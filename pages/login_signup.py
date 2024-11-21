import streamlit as st

def login_signup_page(mongo_ops):
    # Set default current page if not already set
    if "current_page" not in st.session_state:
        st.session_state.current_page = "login"

    # Login Page
    if st.session_state.current_page == "login":
        st.sidebar.title("Welcome to MedAI")
        st.sidebar.markdown("Please login or signup to continue.")

        st.header("Login")
        with st.form("login_form"):
            email = st.text_input("Email", placeholder="Enter your email")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            submitted = st.form_submit_button("Login")

        if submitted:
            if mongo_ops.login(email, password):
                st.session_state.logged_in = True
                st.session_state.current_page = "dashboard"  # Switch to dashboard
            else:
                st.error("Invalid email or password!")

    # Signup Page
    elif st.session_state.current_page == "signup":
        st.sidebar.title("Welcome to MedAI")
        st.sidebar.markdown("Please login or signup to continue.")

        st.header("Signup")
        with st.form("signup_form"):
            name = st.text_input("Name", placeholder="Enter your name")
            email = st.text_input("Email", placeholder="Enter your email")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
            submitted = st.form_submit_button("Signup")

        if submitted:
            if password != confirm_password:
                st.error("Passwords do not match!")
            elif mongo_ops.signup(name, email, password):
                st.success("Signup successful! You can now login.")
                st.session_state.current_page = "login"  # Switch back to login page
            else:
                st.error("Email already exists!")

    # Sidebar Navigation between Login and Signup
    if st.sidebar.button("Switch to Signup" if st.session_state.current_page == "login" else "Switch to Login"):
        st.session_state.current_page = "signup" if st.session_state.current_page == "login" else "login"

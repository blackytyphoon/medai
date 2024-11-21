import streamlit as st
from pages.login_signup import login_signup_page
from pages.dashboard import dashboard_page
from utils.mongo_operations import MongoDBOperations

uri = "mongodb+srv://medai:Wb9Kpn2WLx7Bfwyx@cluster0.0bjj1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo_ops = MongoDBOperations(uri)

def main():
    st.set_page_config(
        page_title="MedAI",
        page_icon="💉",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Initialize session state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # Render appropriate page
    if st.session_state.logged_in:
        dashboard_page(mongo_ops)
    else:
        login_signup_page(mongo_ops)

    # Close MongoDB connection
    mongo_ops.close_connection()

if __name__ == "__main__":
    main()

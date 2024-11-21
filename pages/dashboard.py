import streamlit as st
from pages.add_data import add_data_page
from pages.diagnose import diagnose_page
from pages.cancer import cancer_page

def dashboard_page(mongo_ops):
    st.sidebar.title("MedAI Dashboard")
    menu = st.sidebar.radio(
        "Navigation",
        ["Add Medical Data", "Diagnose", "Cancer", "Logout"],
        index=0,
    )

    # Logout logic
    if menu == "Logout":
        st.session_state.logged_in = False
        st.sidebar.success("You have been logged out!")
        st.experimental_rerun()

    # Display selected page
    if menu == "Add Medical Data":
        add_data_page()
    elif menu == "Diagnose":
        diagnose_page()
    elif menu == "Cancer":
        cancer_page()

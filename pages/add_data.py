import streamlit as st

def add_data_page():
    st.header("Add Medical Data")
    with st.form("add_data_form"):
        name = st.text_input("Patient Name", placeholder="Enter full name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        condition = st.text_area("Condition Details", placeholder="Enter condition details")
        submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.success(f"Medical data for {name} added successfully!")

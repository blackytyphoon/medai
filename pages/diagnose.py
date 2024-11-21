import streamlit as st

def diagnose_page():
    st.header("Diagnose")
    symptoms = st.multiselect(
        "Select Symptoms",
        ["Fever", "Cough", "Fatigue", "Chest Pain", "Shortness of Breath"]
    )
    if st.button("Diagnose"):
        if symptoms:
            st.success("Diagnosis complete! Condition: Sample Diagnosis.")
        else:
            st.warning("Please select at least one symptom.")

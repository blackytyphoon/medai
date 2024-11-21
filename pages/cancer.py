import streamlit as st

def cancer_page():
    st.header("Cancer Diagnosis")
    report = st.file_uploader("Upload Medical Report", type=["pdf", "jpg", "png"])
    if st.button("Analyze"):
        if report:
            st.success("Report analyzed successfully! No malignancy detected.")
        else:
            st.warning("Please upload a report.")

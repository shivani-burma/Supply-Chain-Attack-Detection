import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Supply Chain Attack Detection",
    page_icon="🛡️",
    layout="wide"
)

# Main Title
st.title("🛡️ Software Supply Chain Attack Detection System")

st.markdown("""
### Detecting Supply Chain and Dependency Confusion Attacks in Open-Source Ecosystems
""")

st.write("---")

# Project Overview
st.subheader("Project Overview")

st.write("""
This dashboard presents a machine learning framework for detecting
suspicious Python packages associated with software supply chain
and dependency confusion attacks.

The system was developed using package metadata collected from
the Python Package Index (PyPI) and applies machine learning
techniques to classify packages as legitimate or suspicious.
""")

# Dataset Information
st.subheader("Dataset Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Dataset Size", "802")

with col2:
    st.metric("Features", "9")

with col3:
    st.metric("Classes", "2")

# Best Model
st.subheader("Selected Model for Deployment")

st.success("Decision Tree Classifier")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Accuracy", "100%")

with col2:
    st.metric("Precision", "100%")

with col3:
    st.metric("Recall", "100.00%")

with col4:
    st.metric("F1-Score", "100%")

st.write("---")

st.info("""
Use the navigation menu on the left to access:

• Home

• Package Risk Prediction

• Dataset Analytics

""")

# Footer
st.write("---")

st.caption(
    "MSc Project | Software Supply Chain Attack Detection using Machine Learning"
)
import streamlit as st
import pandas as pd

st.title("Project Overview")

df = pd.read_csv("data/enhanced_final_detection_dataset.csv")

# ------------------------
# Project Description
# ------------------------

st.subheader("Project Description")

st.write("""
This project presents a lightweight machine learning framework for
detecting suspicious Python packages associated with software supply
chain attacks using package metadata and package name similarity.
""")

# ------------------------
# Dataset Summary
# ------------------------

st.subheader("Dataset Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Records", len(df))

with col2:
    st.metric("Features", len(df.columns))

with col3:
    st.metric("Classes", df["Label"].nunique())

# ------------------------
# Selected Model
# ------------------------

st.subheader("Selected Model for Deployment")

st.success("Decision Tree Classifier")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Accuracy", "100%")

with col2:
    st.metric("Precision", "100%")

with col3:
    st.metric("Recall", "100%")

with col4:
    st.metric("F1-Score", "100%")

# ------------------------
# External Validation
# ------------------------

st.subheader("External Validation")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Packages Tested", "100")

with col2:
    st.metric("Detected", "78")

with col3:
    st.metric("Detection Rate", "78%")

st.info("""
The internal evaluation achieved perfect classification on the constructed
training dataset. External validation using 100 real malicious packages
from the OpenSSF Malicious Packages Repository achieved a 78% detection
rate, providing a more realistic assessment of the framework's
generalisation performance.
""")
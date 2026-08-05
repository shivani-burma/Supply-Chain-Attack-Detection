import streamlit as st
import pandas as pd
import joblib

st.title("Package Risk Prediction")

# Load trained model
model = joblib.load("models/best_supply_chain_model.pkl")

st.subheader("Enter Package Features")

similarity_score = st.number_input(
    "Similarity Score",
    min_value=0.0,
    max_value=100.0,
    value=90.0,
    step=0.1
)

name_length = st.number_input(
    "Package Name Length",
    min_value=1,
    value=8
)

summary_length = st.number_input(
    "Summary Length",
    min_value=0,
    value=100
)

release_count = st.number_input(
    "Release Count",
    min_value=0,
    value=10
)

package_age = st.number_input(
    "Package Age (Days)",
    min_value=0,
    value=365
)

if st.button("Predict Risk"):

    data = pd.DataFrame(
        [[
            similarity_score,
            name_length,
            summary_length,
            release_count,
            package_age
        ]],
        columns=[
            "SimilarityScore",
            "NameLength",
            "SummaryLength",
            "ReleaseCount",
            "PackageAgeDays"
        ]
    )

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.error("⚠️ Suspicious Package Detected")
        st.metric("Risk Level", "High Risk")
    else:
        st.success("✅ Legitimate Package")
        st.metric("Risk Level", "Low Risk")
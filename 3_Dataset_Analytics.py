import streamlit as st
import pandas as pd

st.title("Dataset Analytics")

df = pd.read_csv(
    "data/enhanced_final_detection_dataset.csv"
)

st.subheader("Dataset Information")

st.write(df.head())

st.subheader("Dataset Shape")

st.write(df.shape)

st.subheader("Class Distribution")

st.image(
    "plots/class_distribution.png"
)

st.subheader("Correlation Heatmap")

st.image(
    "plots/correlation_heatmap.png"
)

st.subheader("Feature Importance")

st.image(
    "plots/feature_importance.png"
)

st.subheader("Model Comparison")

st.image(
    "plots/model_comparison.png"
)

st.subheader("ROC Curve")

st.image(
    "plots/roc_curve.png"
)

st.subheader("Logistic Regression Confusion Matrix")

st.image(
    "plots/lr_confusion_matrix.png"
)

st.subheader("Decision Tree Confusion Matrix")

st.image(
    "plots/dt_confusion_matrix.png"
)

st.subheader("Random Forest Confusion Matrix")

st.image(
    "plots/rf_confusion_matrix.png"
)
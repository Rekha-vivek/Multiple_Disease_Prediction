import streamlit as st
import pandas as pd
import numpy as np
import pickle

# -------------------------------------------------
# LOAD TRAINED MODEL, SCALER, AND FEATURE COLUMNS
# -------------------------------------------------

with open("liver_model.pkl", "rb") as file:
    liver_model = pickle.load(file)

with open("liver_scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

with open("liver_features.pkl", "rb") as file:
    feature_columns_liver = pickle.load(file)

# -------------------------------------------------
# STREAMLIT PAGE CONFIG
# -------------------------------------------------

st.set_page_config(page_title="Liver Disease Prediction", layout="centered")

st.title("🩺 Liver Disease Prediction System")
st.markdown("Enter patient details below to predict liver disease risk.")

# -------------------------------------------------
# USER INPUT SECTION
# -------------------------------------------------

age = st.number_input("Age", min_value=1, max_value=100, value=40)

gender = st.selectbox("Gender", ["Male","Female"])

total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0, value=1.0)
direct_bilirubin = st.number_input("Direct Bilirubin", min_value=0.0, value=0.5)
alk_phos = st.number_input("Alkaline Phosphotase", min_value=0.0, value=200.0)
alt = st.number_input("Alamine Aminotransferase", min_value=0.0, value=40.0)
ast = st.number_input("Aspartate Aminotransferase", min_value=0.0, value=40.0)
total_proteins = st.number_input("Total Protiens", min_value=0.0, value=6.5)
albumin = st.number_input("Albumin", min_value=0.0, value=3.0)
agr = st.number_input("Albumin and Globulin Ratio", min_value=0.0, value=1.0)

# -------------------------------------------------
# PREDICTION LOGIC
# -------------------------------------------------

if st.button("Predict Liver Disease"):

    # Create empty dataframe with correct training columns
    input_df = pd.DataFrame(columns=feature_columns_liver)
    input_df.loc[0] = 0

    # Encode Gender
    gender_encoded = 1 if gender == "Male" else 0

    # Fill values (must match training column names exactly)
    input_df["Age"] = age
    input_df["Gender"] = gender_encoded
    input_df["Total_Bilirubin"] = total_bilirubin
    input_df["Direct_Bilirubin"] = direct_bilirubin
    input_df["Alkaline_Phosphotase"] = alk_phos
    input_df["Alamine_Aminotransferase"] = alt
    input_df["Aspartate_Aminotransferase"] = ast
    input_df["Total_Protiens"] = total_proteins  # Note spelling matches training
    input_df["Albumin"] = albumin
    input_df["Albumin_and_Globulin_Ratio"] = agr

    # Scale input
    input_scaled = scaler.transform(input_df)

    # Predict
    prediction = liver_model.predict(input_scaled)[0]
    probability = liver_model.predict_proba(input_scaled)[0][1]

    # Display probability
    st.subheader("Prediction Result")
    st.write(f"🧪 Probability of Liver Disease: {probability:.2f}")

    if prediction == 1:
        st.error("⚠ Liver Disease Detected")
    else:
        st.success("✅ No Liver Disease Detected")
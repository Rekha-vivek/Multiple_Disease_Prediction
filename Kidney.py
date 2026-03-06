import streamlit as st
import pandas as pd
import numpy as np
import pickle

# -------------------------------------------------
# LOAD TRAINED MODEL, SCALER, AND FEATURE COLUMNS
# -------------------------------------------------

with open("kidney_model.pkl", "rb") as file:
    kidney_model = pickle.load(file)

with open("kidney_scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

with open("kidney_features.pkl", "rb") as file:
    feature_columns_kidney = pickle.load(file)

# -------------------------------------------------
# STREAMLIT PAGE CONFIG
# -------------------------------------------------

st.set_page_config(page_title="Kidney Disease Prediction", layout="centered")

st.title("🩺 Chronic Kidney Disease Prediction")
st.markdown("Enter patient details below to predict CKD risk.")

# -------------------------------------------------
# USER INPUT SECTION
# -------------------------------------------------

age = st.number_input("Age", 1, 120, 40)
bp = st.number_input("Blood Pressure", 0, 200, 80)
sg = st.number_input("Specific Gravity", value=1.020)
al = st.number_input("Albumin", 0.0, 5.0, 1.0)
su = st.number_input("Sugar", 0.0, 5.0, 0.0)

rbc = st.selectbox("Red Blood Cells", ["normal", "abnormal"])
pc = st.selectbox("Pus Cell", ["normal", "abnormal"])
pcc = st.selectbox("Pus Cell Clumps", ["present", "notpresent"])
ba = st.selectbox("Bacteria", ["present", "notpresent"])

bgr = st.number_input("Blood Glucose Random", 0.0, 500.0, 120.0)
bu = st.number_input("Blood Urea", 0.0, 300.0, 40.0)
sc = st.number_input("Serum Creatinine", 0.0, 20.0, 1.2)
sod = st.number_input("Sodium", 0.0, 200.0, 140.0)
pot = st.number_input("Potassium", 0.0, 10.0, 4.5)

hemo = st.number_input("Hemoglobin", 0.0, 20.0, 15.0)
pcv = st.number_input("Packed Cell Volume", 0.0, 60.0, 44.0)
wc = st.number_input("White Blood Cell Count", 0.0, 20000.0, 8000.0)
rc = st.number_input("Red Blood Cell Count", 0.0, 10.0, 5.0)

htn = st.selectbox("Hypertension", ["yes", "no"])
dm = st.selectbox("Diabetes Mellitus", ["yes", "no"])
cad = st.selectbox("Coronary Artery Disease", ["yes", "no"])
appet = st.selectbox("Appetite", ["good", "poor"])
pe = st.selectbox("Pedal Edema", ["yes", "no"])
ane = st.selectbox("Anemia", ["yes", "no"])

# -------------------------------------------------
# PREDICTION LOGIC
# -------------------------------------------------

if st.button("Predict Kidney Disease"):

    input_df = pd.DataFrame(columns=feature_columns_kidney)
    input_df.loc[0] = 0

    # Fill numeric values
    input_df["age"] = age
    input_df["bp"] = bp
    input_df["sg"] = sg
    input_df["al"] = al
    input_df["su"] = su
    input_df["bgr"] = bgr
    input_df["bu"] = bu
    input_df["sc"] = sc
    input_df["sod"] = sod
    input_df["pot"] = pot
    input_df["hemo"] = hemo
    input_df["pcv"] = pcv
    input_df["wc"] = wc
    input_df["rc"] = rc

    # Manual encoding (must match training encoding)
    input_df["rbc"] = 1 if rbc == "normal" else 0
    input_df["pc"] = 1 if pc == "normal" else 0
    input_df["pcc"] = 1 if pcc == "present" else 0
    input_df["ba"] = 1 if ba == "present" else 0

    input_df["htn"] = 1 if htn == "yes" else 0
    input_df["dm"] = 1 if dm == "yes" else 0
    input_df["cad"] = 1 if cad == "yes" else 0
    input_df["appet"] = 1 if appet == "good" else 0
    input_df["pe"] = 1 if pe == "yes" else 0
    input_df["ane"] = 1 if ane == "yes" else 0

    # Scale
    input_scaled = scaler.transform(input_df)

    # Predict
    prediction = kidney_model.predict(input_scaled)[0]
    probability = kidney_model.predict_proba(input_scaled)[0][1]

    st.subheader("Prediction Result")
    st.write(f"🧪 Probability of CKD: {probability:.2f}")

    if prediction == 1:
        st.error("⚠ Chronic Kidney Disease Detected")
    else:
        st.success("✅ No Kidney Disease Detected")
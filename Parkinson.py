import streamlit as st
import pandas as pd
import numpy as np
import pickle

# -------------------------------------------------
# LOAD TRAINED MODEL, SCALER, AND FEATURE COLUMNS
# -------------------------------------------------

with open("parkinson_model.pkl", "rb") as file:
    parkinson_model = pickle.load(file)

with open("parkinson_scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

with open("parkinson_features.pkl", "rb") as file:
    feature_columns_parkinson = pickle.load(file)

# -------------------------------------------------
# STREAMLIT PAGE CONFIG
# -------------------------------------------------

st.set_page_config(page_title="Parkinson Disease Prediction", layout="centered")

st.title("🧠 Parkinson's Disease Prediction System")
st.markdown("Enter voice measurement details below to predict Parkinson’s risk.")

# -------------------------------------------------
# USER INPUT SECTION
# -------------------------------------------------

# ⚠ IMPORTANT:
# These feature names must match EXACTLY your training dataset columns.

fo = st.number_input("MDVP:Fo(Hz)", value=120.0)
fhi = st.number_input("MDVP:Fhi(Hz)", value=150.0)
flo = st.number_input("MDVP:Flo(Hz)", value=75.0)
jitter = st.number_input("MDVP:Jitter(%)", value=0.005)
jitter_abs = st.number_input("MDVP:Jitter(Abs)", value=0.00003)
rap = st.number_input("MDVP:RAP", value=0.002)
ppq = st.number_input("MDVP:PPQ", value=0.002)
ddp = st.number_input("Jitter:DDP", value=0.006)

shimmer = st.number_input("MDVP:Shimmer", value=0.03)
shimmer_db = st.number_input("MDVP:Shimmer(dB)", value=0.3)
apq3 = st.number_input("Shimmer:APQ3", value=0.02)
apq5 = st.number_input("Shimmer:APQ5", value=0.03)
apq = st.number_input("MDVP:APQ", value=0.03)
dda = st.number_input("Shimmer:DDA", value=0.06)

nhr = st.number_input("NHR", value=0.02)
hnr = st.number_input("HNR", value=20.0)

rpde = st.number_input("RPDE", value=0.5)
dfa = st.number_input("DFA", value=0.7)
spread1 = st.number_input("spread1", value=-5.0)
spread2 = st.number_input("spread2", value=0.2)
d2 = st.number_input("D2", value=2.0)
ppe = st.number_input("PPE", value=0.2)

# -------------------------------------------------
# PREDICTION LOGIC
# -------------------------------------------------

if st.button("Predict Parkinson's Disease"):

    # Create empty dataframe with correct training columns
    input_df = pd.DataFrame(columns=feature_columns_parkinson)
    input_df.loc[0] = 0

    # Fill values (must match training column names exactly)
    input_df["MDVP:Fo(Hz)"] = fo
    input_df["MDVP:Fhi(Hz)"] = fhi
    input_df["MDVP:Flo(Hz)"] = flo
    input_df["MDVP:Jitter(%)"] = jitter
    input_df["MDVP:Jitter(Abs)"] = jitter_abs
    input_df["MDVP:RAP"] = rap
    input_df["MDVP:PPQ"] = ppq
    input_df["Jitter:DDP"] = ddp

    input_df["MDVP:Shimmer"] = shimmer
    input_df["MDVP:Shimmer(dB)"] = shimmer_db
    input_df["Shimmer:APQ3"] = apq3
    input_df["Shimmer:APQ5"] = apq5
    input_df["MDVP:APQ"] = apq
    input_df["Shimmer:DDA"] = dda

    input_df["NHR"] = nhr
    input_df["HNR"] = hnr
    input_df["RPDE"] = rpde
    input_df["DFA"] = dfa
    input_df["spread1"] = spread1
    input_df["spread2"] = spread2
    input_df["D2"] = d2
    input_df["PPE"] = ppe

    # Scale input
    input_scaled = scaler.transform(input_df)

    input_scaled = pd.DataFrame(
    input_scaled,
    columns=feature_columns_parkinson
)

    # Predict
    prediction = parkinson_model.predict(input_scaled)[0]
    probability = parkinson_model.predict_proba(input_scaled)[0][1]

    # Display Result
    st.subheader("Prediction Result")
    st.write(f"🧪 Probability of Parkinson's Disease: {probability:.2f}")

    if prediction == 1:
        st.error("⚠ Parkinson's Disease Detected")
    else:
        st.success("✅ No Parkinson's Disease Detected")
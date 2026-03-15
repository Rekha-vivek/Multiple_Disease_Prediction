import streamlit as st
import pandas as pd
import pickle

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Multiple Disease Prediction System",
    page_icon="🏥",
    layout="centered"
)

# -------------------------------------------------
# CUSTOM UI STYLING
# -------------------------------------------------

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background-color: #e6f4ff;
    }

    /* Title styling */
    h1 {
        color: #003366;
        text-align: center;
        font-weight: bold;
    }

    h2, h3 {
        color: #004080;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #003366;
    }

    section[data-testid="stSidebar"] label {
        color: white;
        font-weight: bold;
    }

    section[data-testid="stSidebar"] .css-1d391kg {
        color: white;
    }

    /* Buttons */
    .stButton>button {
        background-color: #ffcc00;
        color: black;
        font-weight: bold;
        border-radius: 10px;
        height: 45px;
        width: 100%;
    }

    .stButton>button:hover {
        background-color: #ffdb4d;
    }

    /* Result box */
    .result-box {
        background-color: #fff3cd;
        padding: 15px;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# LOAD MODELS
# -------------------------------------------------

liver_model = pickle.load(open("liver_model.pkl", "rb"))
liver_scaler = pickle.load(open("liver_scaler.pkl", "rb"))
liver_features = pickle.load(open("liver_features.pkl", "rb"))

kidney_model = pickle.load(open("kidney_model.pkl", "rb"))
kidney_scaler = pickle.load(open("kidney_scaler.pkl", "rb"))
kidney_features = pickle.load(open("kidney_features.pkl", "rb"))

parkinson_model = pickle.load(open("parkinson_model.pkl", "rb"))
parkinson_scaler = pickle.load(open("parkinson_scaler.pkl", "rb"))
parkinson_features = pickle.load(open("parkinson_features.pkl", "rb"))

# -------------------------------------------------
# TITLE
# -------------------------------------------------

st.markdown("<h1>🏥 Multiple Disease Prediction System</h1>", unsafe_allow_html=True)

st.info(
    "This system predicts Liver Disease, Kidney Disease, and Parkinson’s Disease using trained Machine Learning models."
)

# -------------------------------------------------
# SIDEBAR MENU
# -------------------------------------------------

disease = st.sidebar.selectbox(
    "Select Disease Prediction",
    ("Liver Disease", "Kidney Disease", "Parkinson Disease")
)

# -------------------------------------------------
# LIVER DISEASE
# -------------------------------------------------

if disease == "Liver Disease":

    st.header("🩺 Liver Disease Prediction")

    age = st.number_input("Age", 1, 100, 40)
    gender = st.selectbox("Gender", ["Male", "Female"])

    total_bilirubin = st.number_input("Total Bilirubin", 0.0, 10.0, 1.0)
    direct_bilirubin = st.number_input("Direct Bilirubin", 0.0, 10.0, 0.5)
    alk_phos = st.number_input("Alkaline Phosphotase", 0.0, 500.0, 200.0)
    alt = st.number_input("Alanine Aminotransferase", 0.0, 500.0, 40.0)
    ast = st.number_input("Aspartate Aminotransferase", 0.0, 500.0, 40.0)
    total_proteins = st.number_input("Total Proteins", 0.0, 10.0, 6.5)
    albumin = st.number_input("Albumin", 0.0, 10.0, 3.0)
    agr = st.number_input("Albumin and Globulin Ratio", 0.0, 5.0, 1.0)

    if st.button("Predict Liver Disease"):

        df = pd.DataFrame(columns=liver_features)
        df.loc[0] = 0

        gender_encoded = 1 if gender == "Male" else 0

        df["Age"] = age
        df["Gender"] = gender_encoded
        df["Total_Bilirubin"] = total_bilirubin
        df["Direct_Bilirubin"] = direct_bilirubin
        df["Alkaline_Phosphotase"] = alk_phos
        df["Alamine_Aminotransferase"] = alt
        df["Aspartate_Aminotransferase"] = ast
        df["Total_Protiens"] = total_proteins
        df["Albumin"] = albumin
        df["Albumin_and_Globulin_Ratio"] = agr

        scaled = liver_scaler.transform(df)

        prediction = liver_model.predict(scaled)[0]
        probability = liver_model.predict_proba(scaled)[0][1]

        st.subheader("Prediction Result")
        st.write(f"Probability: {probability:.2f}")

        if prediction == 1:
            st.error("⚠ Liver Disease Detected")
        else:
            st.success("✅ No Liver Disease")

# -------------------------------------------------
# KIDNEY DISEASE
# -------------------------------------------------

elif disease == "Kidney Disease":

    st.header("🩸 Kidney Disease Prediction")

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

    if st.button("Predict Kidney Disease"):

        df = pd.DataFrame(columns=kidney_features)
        df.loc[0] = 0

        df["age"] = age
        df["bp"] = bp
        df["sg"] = sg
        df["al"] = al
        df["su"] = su
        df["bgr"] = bgr
        df["bu"] = bu
        df["sc"] = sc
        df["sod"] = sod
        df["pot"] = pot
        df["hemo"] = hemo
        df["pcv"] = pcv
        df["wc"] = wc
        df["rc"] = rc

        df["rbc"] = 1 if rbc == "normal" else 0
        df["pc"] = 1 if pc == "normal" else 0
        df["pcc"] = 1 if pcc == "present" else 0
        df["ba"] = 1 if ba == "present" else 0
        df["htn"] = 1 if htn == "yes" else 0
        df["dm"] = 1 if dm == "yes" else 0
        df["cad"] = 1 if cad == "yes" else 0
        df["appet"] = 1 if appet == "good" else 0
        df["pe"] = 1 if pe == "yes" else 0
        df["ane"] = 1 if ane == "yes" else 0

        scaled = kidney_scaler.transform(df)

        prediction = kidney_model.predict(scaled)[0]
        probability = kidney_model.predict_proba(scaled)[0][1]

        st.subheader("Prediction Result")
        st.write(f"Probability: {probability:.2f}")

        if prediction == 1:
            st.error("⚠ Kidney Disease Detected")
        else:
            st.success("✅ No Kidney Disease")

# -------------------------------------------------
# PARKINSON DISEASE
# -------------------------------------------------

else:

    st.header("🧠 Parkinson Disease Prediction")

    fo = st.number_input("Fo (Hz)", 120.0)
    fhi = st.number_input("Fhi (Hz)", 150.0)
    flo = st.number_input("Flo (Hz)", 75.0)
    jitter = st.number_input("Jitter", 0.005)
    shimmer = st.number_input("Shimmer", 0.03)
    nhr = st.number_input("NHR", 0.02)
    hnr = st.number_input("HNR", 20.0)
    rpde = st.number_input("RPDE", 0.5)
    dfa = st.number_input("DFA", 0.7)
    spread1 = st.number_input("Spread1", -5.0)
    spread2 = st.number_input("Spread2", 0.2)
    d2 = st.number_input("D2", 2.0)
    ppe = st.number_input("PPE", 0.2)

    if st.button("Predict Parkinson Disease"):

        df = pd.DataFrame(columns=parkinson_features)
        df.loc[0] = 0

        df["MDVP:Fo(Hz)"] = fo
        df["MDVP:Fhi(Hz)"] = fhi
        df["MDVP:Flo(Hz)"] = flo
        df["MDVP:Jitter(%)"] = jitter
        df["MDVP:Shimmer"] = shimmer
        df["NHR"] = nhr
        df["HNR"] = hnr
        df["RPDE"] = rpde
        df["DFA"] = dfa
        df["spread1"] = spread1
        df["spread2"] = spread2
        df["D2"] = d2
        df["PPE"] = ppe

        scaled = parkinson_scaler.transform(df)

        prediction = parkinson_model.predict(scaled)[0]
        probability = parkinson_model.predict_proba(scaled)[0][1]

        st.subheader("Prediction Result")
        st.write(f"Probability: {probability:.2f}")

        if prediction == 1:
            st.error("⚠ Parkinson Disease Detected")
        else:
            st.success("✅ No Parkinson Disease")
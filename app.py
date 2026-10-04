import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Heart Disease Risk Checker", page_icon="❤️")

@st.cache_resource
def load_model():
    return joblib.load("heart_model.joblib")   # one file: encoding + scaling + SVM

model = load_model()

st.title("❤️ Heart Disease Risk Checker")
st.caption("Educational demo built on the Kaggle heart-failure dataset. Not a medical diagnosis.")

with st.form("form"):
    c1, c2 = st.columns(2)
    with c1:
        age = st.number_input("Age (years)", 18, 100, 50)
        sex = st.radio("Sex", ["Male", "Female"], horizontal=True)
        chest = st.selectbox("Chest pain type", [
            "Asymptomatic (no chest pain)",
            "Atypical angina",
            "Non-anginal pain",
            "Typical angina",
        ])
        angina = st.radio("Chest pain during exercise?", ["No", "Yes"], horizontal=True)
    with c2:
        fbs = st.radio("Fasting blood sugar above 120 mg/dl?", ["No", "Yes"], horizontal=True)
        slope = st.selectbox("ST slope on exercise ECG", ["Up", "Flat", "Down"],
                             help="From a stress-test ECG report.")
        oldpeak = st.number_input("ST depression (Oldpeak)", -3.0, 7.0, 0.0, step=0.1,
                                  help="From a stress-test ECG report. Use 0 if normal.")
    go = st.form_submit_button("Check risk", use_container_width=True)

if go:
    row = pd.DataFrame([{
        "Age": age,
        "Sex": "M" if sex == "Male" else "F",
        "ChestPainType": {"Asymptomatic (no chest pain)": "ASY", "Atypical angina": "ATA",
                          "Non-anginal pain": "NAP", "Typical angina": "TA"}[chest],
        "FastingBS": 1 if fbs == "Yes" else 0,
        "ExerciseAngina": "Y" if angina == "Yes" else "N",
        "ST_Slope": slope,
        "Oldpeak": oldpeak,
    }])
    prob = float(model.predict_proba(row)[0][1])

    st.subheader(f"Estimated risk: {prob:.0%}")
    st.progress(prob)
    if prob < 0.40:
    st.success("The model estimates a lower risk score.")
elif prob <= 0.60:
    st.warning("The model result is borderline. Consider professional medical evaluation.")
else:
    st.error("The model estimates a higher risk score. Please consult a doctor.")
    st.caption("Trained on 918 patients, ~86% accuracy on held-out data. "
               "A low score does not rule out heart disease.")

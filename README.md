# ❤️ Heart Disease Risk Prediction

A machine learning-powered web application that estimates the likelihood of heart disease based on selected clinical and health-related parameters.

The application uses a trained machine learning model integrated with **Streamlit** to provide an interactive interface where users can enter patient information and receive an estimated risk score.

## 🚀 Live Demo

👉 [Open the Live App](https://heart-disease-prediction-4xbtpms7ygoerrhbgeprts.streamlit.app)

## 🚀 Features

- Interactive web interface built with Streamlit
- Heart disease risk estimation using a trained ML model
- Input validation and user-friendly controls
- Probability-based risk prediction
- Visual risk indicator with progress bar
- Simple and responsive interface

## 🧠 Machine Learning

The prediction model was trained on a heart disease dataset containing **918 patient records**. The application uses a trained model with preprocessing, encoding, and scaling incorporated into the saved model pipeline.

The application considers features such as:

- Age
- Sex
- Chest Pain Type
- Fasting Blood Sugar
- Exercise-Induced Angina
- ST Slope
- ST Depression (Oldpeak)

The model achieved approximately **86% accuracy on held-out test data**.

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Scikit-learn**
- **Joblib**
- **Streamlit**

## 📊 How It Works

```text
User Input
    ↓
Data Preprocessing
    ↓
Trained Machine Learning Model
    ↓
Probability Prediction
    ↓
Estimated Heart Disease Risk
```

## ⚙️ Run Locally

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/heart-disease-prediction.git
cd heart-disease-prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will then be available in your browser.

## ⚠️ Disclaimer

This project is developed for **educational and demonstration purposes only**. The prediction produced by the application should not be considered a medical diagnosis or a substitute for professional medical advice.

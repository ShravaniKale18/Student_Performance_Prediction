import pickle
import streamlit as st
import pandas as pd


with open("student_score_model.pkl", "rb") as file:
    model = pickle.load(file)


st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Performance Prediction")
st.write("Predict the Final Exam Score.")

gender = st.selectbox("Gender", ["Male", "Female"])

age = st.slider("Age", 17, 26, 20)

study = st.slider("Study Hours Per Day", 0.0, 10.0, 4.0)

attendance = st.slider("Attendance Percentage", 50.0, 100.0, 80.0)

previous = st.slider("Previous Exam Score", 0.0, 100.0, 60.0)

assignments = st.slider("Assignments Completed", 0, 20, 10)

sleep = st.slider("Sleep Hours", 3.0, 10.0, 7.0)

social = st.slider("Social Media Hours", 0.0, 10.0, 3.0)

extra = st.selectbox("Extra Curricular", ["Yes", "No"])

stress = st.slider("Stress Level", 1, 10, 5)

# Encode categorical variables
gender = 1 if gender == "Male" else 0
extra = 1 if extra == "Yes" else 0

# Prediction
if st.button("Predict Score"):

    input_data = pd.DataFrame([{
        "Gender": gender,
        "Age": age,
        "Study_Hours_Per_Day": study,
        "Attendance_Percentage": attendance,
        "Previous_Exam_Score": previous,
        "Assignments_Completed": assignments,
        "Sleep_Hours": sleep,
        "Social_Media_Hours": social,
        "Extra_Curricular": extra,
        "Stress_Level": stress
    }])

    prediction = model.predict(input_data)[0]

    st.success(f"🎯 Predicted Final Exam Score: {prediction:.2f}")
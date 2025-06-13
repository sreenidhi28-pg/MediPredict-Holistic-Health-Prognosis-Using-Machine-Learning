# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 00:38:38 2024

@author: kanth
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Medi-Predict",
                   layout="wide",
                   page_icon="🧑‍⚕️",
                   initial_sidebar_state="expanded")


# Function to display summary and symptoms
def display_summary_disease(disease_name):
    if disease_name == "Diabetes":
        st.markdown("### Diabetes")
        st.write("Diabetes is a chronic condition that affects how your body turns food into energy.")
        st.write("**Common Symptoms:**")
        st.write("- Increased thirst and urination")
        st.write("- Fatigue")
        st.write("- Blurred vision")
        st.write("**Prediction Model:**")
        st.write("Please input the required features in the form below to predict diabetes.")
    elif disease_name == "Heart Disease":
        st.markdown("### Heart Disease")
        st.write("Heart disease refers to several conditions that affect the heart.")
        st.write("**Common Symptoms:**")
        st.write("- Chest pain or discomfort")
        st.write("- Shortness of breath")
        st.write("- Nausea or lightheadedness")


# loading the saved models

diabetes_model = pickle.load(open(r'C:\Users\ssree\Downloads\Mini Project\diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(r'C:\Users\ssree\Downloads\Mini Project\heart_disease_model.sav', 'rb'))

#  sidebar for navigation
with st.sidebar:
    selected = option_menu('MediPredict',

                           ['Home',
                            'Diabetes',
                            'Heart Disease'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'person', 'heart'],
                           default_index=0)


# Display content based on navigation choice
if selected == "Home":
    st.title("Welcome to Medi-Predict")
    st.write("At our Disease Prediction Platform, we leverage cutting-edge machine learning techniques to provide accurate predictions for two prevalent health conditions: diabetes and heart disease. With the power of data-driven insights, we aim to empower individuals to take proactive steps towards better health and well-being.Our platform offers user-friendly interfaces and intuitive functionalities, allowing users to input relevant health parameters effortlessly. Through sophisticated machine learning algorithms, we analyze these inputs to generate personalized predictions regarding the likelihood of diabetes or heart disease.")
    st.write("<p style='text-align: center; font-weight: bold;'>Navigate through the left buttons to predict a disease</p>", unsafe_allow_html=True)
# Diabetes Prediction Page
if selected == 'Diabetes':

    # page title
    st.title('Diabetes')
    display_summary_disease("Diabetes")

    # getting the input data from the user
    st.subheader('**Diabetes Prediction**')
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Predict'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
            # Add tips for managing diabetes
            st.subheader("Tips for Managing Diabetes:")
            st.write("- Maintain a healthy diet rich in fruits, vegetables, and whole grains.")
            st.write("- Monitor your blood sugar levels regularly.")
            st.write("- Engage in regular physical activity, such as walking, swimming, or cycling.")
            st.write("- Take prescribed medications as directed by your healthcare provider.")
            st.write("- Stay hydrated and limit the consumption of sugary beverages.")
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease':

    # page title
    st.title('Heart Disease')
    display_summary_disease("Heart Disease")
    
    st.subheader('**Heart Disease Prediction**')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex(male:1,female:2)')
    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Predict'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
            # Add tips for managing heart disease
            st.subheader("Tips for Managing Heart Disease:")
            st.write("- Follow a heart-healthy diet low in saturated fats, cholesterol, and sodium.")
            st.write("- Engage in regular aerobic exercise, such as walking, jogging, or swimming, to improve heart health.")
            st.write("- Quit smoking and avoid exposure to secondhand smoke to reduce the risk of heart complications.")
            st.write("- Monitor blood pressure and cholesterol levels regularly and take prescribed medications as directed.")
            st.write("- Manage stress through relaxation techniques, mindfulness, or counseling to lower heart disease risk.")
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

    

      



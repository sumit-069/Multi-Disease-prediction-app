import pickle 
import streamlit as st
from streamlit_option_menu import option_menu


diabetes=pickle.load(open("Saved models/diabetes.pkl","rb"))
breastcancer=pickle.load(open("Saved models/BreastCancer.pkl","rb"))
heart=pickle.load(open("Saved models/heart.pkl","rb"))

with st.sidebar:
    selected=option_menu("MultiDisease Prediction System",['Diabetes prediction','Breast Cancer Prediction','Heart Disease prediction'],default_index=0)

    
if(selected=='Diabetes prediction'):
    st.title("Diabetes Prediction")

    pregnancies=st.number_input("Number of pregnancies")
    Glucose=st.number_input("Glucose level")
    BloodPressure=st.number_input("Blood Pressure Value")
    SkinThickness=st.number_input("Skin thickness Value")
    Insulin=st.number_input("Insulin level")
    BMI=st.number_input("BMI value")
    DiabetesPedigreeFunction=st.number_input("Diabetes pedigree Function value")
    Age=st.number_input("Age of the person")

    diabetes_ans=''
    if st.button('Diabetes Test Result'):
        diabetes_pred=diabetes.predict([[pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

        if(diabetes_pred[0]==1):
            diabetes_ans='The person is Diabetic'
        else:
            diabetes_ans='The person is not Diabetic'
    st.success(diabetes_ans)



if(selected=='Breast Cancer Prediction'):
    st.title("Breast Cancer Prediction")
    col1,col2,col3,col4=st.columns(4)
    with col1:
        radius_mean=st.number_input("Radius mean of tumor")
    with col2:
        texture_mean=st.number_input("Texture mean of tumor")
    with col3:
        perimeter_mean=st.number_input("Mean Perimeter of tumor")
    with col1:
        area_mean=st.number_input("Mean Area of tumor")
    with col2:
        smoothness_mean=st.number_input("Mean Smoothness of tumor")
    with col3:
        compactness_mean=st.number_input("Mean Compactness of tumor")
    with col1:
        symmetry_mean=st.number_input("Mean symmetry of tumor")
    with col2:
        fractal_dimension_mean=st.number_input("Mean fractal dimension of tumor")
    with col3:
        radius_se=st.number_input("Radius of the tumor")
    with col1:
        texture_se=st.number_input("Texture of tumor")
    with col2:
        perimeter_se=st.number_input("Perimeter of tumor")
    with col3:
        area_se=st.number_input("Area of Tumor")
    with col1:
        smoothness_se=st.number_input("Smoothness of tumor")
    with col2:
        compactness_se=st.number_input("Compactness of tumor")
    with col3:
        symmetry_se=st.number_input("Symmetry of tumor")
    with col1:
        fractal_dimension_se=st.number_input("Fractal dimension of tumor")
    with col2:
        radius_worst=st.number_input("Worst radius of tumor")
    with col3:
        texture_worst=st.number_input("Worst texture of tumor")
    with col1:
        perimeter_worst=st.number_input("Worst perimeter of tumor")
    with col2:
        area_worst=st.number_input("Worst area of tumor")
    with col3:
        smoothness_worst=st.number_input("Worst Smoothness of tumor")
    with col1:
        concave_points_worst=st.number_input("Worst concae points of tumor")
    with col2:
        symmetry_worst=st.number_input("Worst symmetry of tumor")
    with col3:
        fractal_dimension_worst=st.number_input("Worst fractal dimension of tumor")


    ans=''
    if st.button("Breast Cancer Prediction"):
        cancer=breastcancer.predict([[radius_mean,texture_mean,perimeter_mean,
        area_mean,smoothness_mean,compactness_mean,symmetry_mean,fractal_dimension_mean,
        radius_se,texture_se,perimeter_se,area_se,smoothness_se,
        compactness_se,symmetry_se,
        fractal_dimension_se,radius_worst,texture_worst,
        perimeter_worst,area_worst,smoothness_worst,concave_points_worst,
        symmetry_worst,fractal_dimension_worst]])

        if(cancer[0]==1):
            ans='You have Malignant Tumor'
        else:
            ans='You have Benign Tumor'

    st.success(ans)



if(selected=='Heart Disease prediction'):
    st.title("Heart disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

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

   
    heart_diagnosis = ''

    

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

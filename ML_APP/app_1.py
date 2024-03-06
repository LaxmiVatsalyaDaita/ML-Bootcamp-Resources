import numpy as np
import streamlit as st 
import pickle 

import warnings
warnings.filterwarnings("ignore")

# loading the saved model
loaded_model = pickle.load(open('trained_adb_model.sav', 'rb'))

def sleep_disorder_prediction(input_data):
    input_data_as_np_array = np.asarray(input_data) 

    input_data_reshaped = input_data_as_np_array.reshape(1,-1) 

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    pred = loaded_model.predict_proba(input_data_reshaped)
    risk = pred[:,1]
    risk_percent = round(risk[0]*100, 2)
    
    if (prediction[0] == 0):
        return 'the person is not at a risk of sleep disorder'
    else:
        return 'the person is at a risk of sleep disorder'
    
def percentage_of_risk(input_data):
    input_data_as_np_array = np.asarray(input_data) 

    input_data_reshaped = input_data_as_np_array.reshape(1,-1) 

    pred = loaded_model.predict_proba(input_data_reshaped)
    risk = pred[:,1]
    risk_percent = round(risk[0]*100, 2)
    
    print(risk_percent)
    
    return str(risk_percent)
    
    
# UI
st.set_page_config(page_title='Sleep Disorder', page_icon=':zzz:', layout='wide')
st.title(':sleeping: Sleep Disorder RIsk Prediction')
st.markdown('<style>div.block-container{padding-top:1rem;}<style>', unsafe_allow_html=True)


gender = st.selectbox('Gender', ['Male', 'Female'])
age = st.slider('age', 0,100,1)
occupation = st.selectbox('occupation', ['Other', 'Doctor', 'Teacher', 'Nurse', 'Engineer', 'Accountant',
       'Lawyer', 'Salesperson'])
sleepDuration = st.text_input('Sleep duration')
quality = st.slider('Quality of sleep', 0.0, 10.0, step=0.5)
phy = st.text_input('Physical Activity Level')
stressLevel = st.text_input('stress') 
bmi = st.selectbox('bmi', ['Overweight', 'Normal', 'Obese'])
heartRate = st.text_input('heart rate')
steps = st.text_input('steps')
bpUpper = st.text_input('bp upper')
bpLower = st.text_input('bp lower')   

if (gender=='Male'):
    Gender = 1
elif (gender=='Female'):
    Gender = 0
        
if (occupation=='Accountant'):
    Occupation = 0
elif (occupation=='Doctor'):
    Occupation = 1
elif (occupation=='Engineer'):
    Occupation = 2
elif (occupation=='Lawyer'):
    Occupation = 3
elif (occupation=='Nurse'):
    Occupation = 4
elif (occupation=='Other'):
    Occupation = 5
elif (occupation=='Salesperson'):
    Occupation = 6
elif (occupation=='Teacher'):
    Occupation = 7   
        
if (bmi=='Overweight'):
    BMI = 2
elif (bmi=='Normal'):
    BMI = 0
elif (bmi=='Obese'):
    BMI = 1


input_features = [Gender, age, Occupation, sleepDuration, quality, phy, stressLevel, BMI, heartRate, steps, bpUpper, bpLower]

# prediction
diagnosis = ''
percent_of_risk = ''

if st.button('risk prediction'):
    diagnosis = sleep_disorder_prediction(input_features)
st.write(diagnosis)

if st.button('risk percentage'):
    percent_of_risk = percentage_of_risk(input_features)
st.write(percent_of_risk)
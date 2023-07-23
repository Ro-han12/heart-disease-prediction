# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 08:43:28 2023

@author: HP
"""

import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open('C:/Users/HP/Desktop/my projects/heart disease/trained_model .sav','rb'))
def disease_prediction(input_data):
    a=np.asarray(input_data,dtype=float)
    a_new=a.reshape(1,-1)
    prediction=loaded_model.predict(a_new)
    print(prediction)
    #1 has defect and 0 no defect
    if (prediction[0]==0):
      return "person is safe!!!"
    else:
      return "Kindly consult a Cardiolodist"

#working with streamlit

def main():
    st.title("HEART DISEASE PREDICTION WEB-APP")
    age=st.text_input("AGE OF PATIENT")
    sex=st.text_input("GENDER OF PATIENT")
    cp=st.text_input("CHEST PAIN TYPE OF PATIENT")
    trestbpse=st.text_input("bps OF PATIENT")
    chol=st.text_input("cholestrol level OF PATIENT")
    fbs=st.text_input("FASTING BLOOD SUGAR OF PATIENT")
    restec=st.text_input("RESTING ELECTROCARDIOGRAPHIC RESULT OF PATIENT")
    thalach=st.text_input("MAXIMUM HEART RATE OF PATIENT")
    exang=st.text_input("EXERCISE INDUCED ANGINA OF PATIENT")
    oldpeak=st.text_input("ST DEPRESSION INDUCES BY EXERCISE RELATIVE TO REST OF PATIENT")
    slope=st.text_input(" THE ST SEGMENT SHIFT RELATIVE TO EXERCISE-INDUCED INCREMENTS IN HEART RATE OF PATIENT")
    ca=st.text_input("CALCIUM IN HEARTS ARTERIES OF PATIENT")
    thal=st.text_input("THALASSEMIA ie less hemoglobin than nornal OF PATIENT")
    
    
    #code for prediction
    diagnosis=''
    #creating a button
    if st.button('TEST RESULT'):
        diagnosis=disease_prediction([age,sex,cp,trestbpse,chol,fbs,restec,thalach,exang,oldpeak,slope,ca,thal])
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
    
        
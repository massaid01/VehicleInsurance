# -*- coding: utf-8 -*-
"""streamlitapp.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KQoyAAGBXzn_XABME34nFRG24gn82Ac2
"""

from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('Light_GBM')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

st.title('Prediciting Vehicle Insurance in Customers Web App')
st.write('This is a web app to predicting whether existing customers interested or not based on\
         several features that you can see in the sidebar. Please adjust the\
         value of each feature. After that, click on the Predict button at the bottom to\
         see the prediction.')

Identifier = st.number_input(label ='Input your ID number', min_value=1, max_value=381109, value=20)

Gender = st.selectbox('Gender', ['Female', 'Male'])

Age = st.number_input(label = 'Input your age', min_value=24, max_value=85, value=35)

Driving_License = st.selectbox('Do you have a driving license?', [0, 1])

Region_Code = st.number_input(label = 'Input your region code', min_value=1.0, max_value=51.0, value=10.0)

Previously_Insured = st.selectbox('Do you have a previously insured?', [0, 1])

Vehicle_Age = st.selectbox('Input your vehicle age', ['> 2 Years', '1-2 Year', '< 1 Year'])

Vehicle_Damage = st.selectbox('Do you have vehicle damage', ['No', 'Yes'])

Annual_Premium = st.number_input(label = 'Input your annual premium', min_value=2630.0, max_value=540165.0, value=30000.0)

Policy_Sales_Channel = st.number_input(label = 'Input your policy sales channel', min_value=1.0, max_value=163.0, value=30.0)

Vintage = st.number_input(label = 'How long you have been a our customers (in a day)', min_value=10, max_value=299, value=30)

output=""

features = {'id': Identifier, 'Gender': Gender, 'Age': Age,
            'Driving_License': Driving_License, 'Region_Code': Region_Code,
            'Previously_Insured': Previously_Insured, 'Vehicle_Age': Vehicle_Age, 'Vehicle_Damage': Vehicle_Damage,
            'Annual_Premium ': Annual_Premium, 'Policy_Sales_Channel': Policy_Sales_Channel,
            'Vintage': Vintage
            }

features_df  = pd.DataFrame([features])

if st.button("Predict"):
    output = predict(model=model, input_df=input_df)
    output = '$' + str(output)

st.success('The output is {}'.format(output))

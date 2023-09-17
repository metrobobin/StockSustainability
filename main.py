import streamlit as st
import pandas as pd
import numpy as np
import csv
from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from streamlit_lottie import st_lottie
import requests

# Neural Network

def trainNetwork():
    trainingData = loadtxt('trunc_data.csv', delimiter=',')

    inData = trainingData[:,0:8]
    outData = trainingData[:,8]

    model = Sequential()

    model.add(Dense(12, input_shape=(8,), activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.fit(inData, outData, epochs=5, batch_size=3,verbose=0)

    _, accuracy = model.evaluate(inData, outData)
    print('Accuracy: %.2f' % (accuracy*100))

    predictData = loadtxt('test.csv', delimiter=',')
    predictRow = predictData[:,0:8]

    predictions = model.predict(predictRow)
    
    print(predictions[0])
    return (predictions[0])


# UI Builder 
st.set_page_config(page_title="Sustainability Calculator", page_icon=":earth_americas:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Header
st.subheader("Hi, welcome to our Project :wave:")
st.title('Sustainability Calculator :recycle:')

#Animations
lottie_coding = load_lottieurl("https://lottie.host/fd96b7f7-ffac-40f4-8f1c-cabc08b6c3e9/HdkGG4yANf.json")

#Columns for website
with st.container():
     st.write("---")
     left_column, right_column = st.columns(2)
     with left_column:
          RV_title = st.number_input('Revenue Growth')
          
          EB_title = st.number_input("EBITDA[*](https://www.bdc.ca/en/articles-tools/entrepreneur-toolkit/templates-business-guides/glossary/ebitda#:~:text=EBITDA%20is%20short%20for%20earnings,and%20ability%20to%20generate%20cash.)")
          NE_title = st.number_input('Number of Employees')
          Weight_title = st.number_input('Weight %')
          EV_title = st.number_input('Enviornmental Score')
          GoV_title = st.number_input("Government Score[*](https://www.msci.com/documents/1296102/14524248/MSCI+ESG+Research+Controversies+Executive+Summary+Methodology+-++July+2020.pdf/b0a2bb88-2360-1728-b70e-2f0a889b6bd4)")
          SS_title = st.number_input('Social Score')
          ControS_title = st.number_input('Controversial Score[*](https://www.msci.com/documents/1296102/14524248/MSCI+ESG+Research+Controversies+Executive+Summary+Methodology+-++July+2020.pdf/b0a2bb88-2360-1728-b70e-2f0a889b6bd4)')
          SubmitBut = st.button("Calculate", type="primary")
          

with right_column:
     st_lottie(lottie_coding, height=700, loop=True, key="coding")

## Adding background
    
## Removing footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


# Array to make CSV
intervals = np.array([[0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1]])

if SubmitBut:
    intervals[0,0] = (RV_title)
    intervals[0,1] = (EB_title)
    intervals[0,2] = (NE_title)
    intervals[0,3] = (Weight_title)
    intervals[0,4] = (EV_title)
    intervals[0,5] = (GoV_title)
    intervals[0,6] = (SS_title)
    intervals[0,7] = (ControS_title)

    print (intervals)

    with open('test.csv','w') as myfile:
         wr = csv.writer(myfile) #, quoting=csv.QUOTE_ALL)
         wr.writerows(intervals)

    returntype = (trainNetwork())
    with st.container():
        st.header(str(returntype))
        st.subheader('This is your sustainability score. The higher the better!')




 



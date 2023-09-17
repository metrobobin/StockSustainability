import streamlit as st
import pandas as pd
import numpy as np
import csv
from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

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
    
    return (predictions[0])


 # UI Builder 

with open('style.css') as f:
       st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
       project_background = """
       <style>
        height: 100%;
	/* max-height: 600px; */
	width: 1000px;
	background-color: hsla(200,40%,30%,.4);
	background-image:		
		url('https://78.media.tumblr.com/cae86e76225a25b17332dfc9cf8b1121/tumblr_p7n8kqHMuD1uy4lhuo1_540.png'), 
		url('https://78.media.tumblr.com/66445d34fe560351d474af69ef3f2fb0/tumblr_p7n908E1Jb1uy4lhuo1_1280.png'),
		url('https://78.media.tumblr.com/8cd0a12b7d9d5ba2c7d26f42c25de99f/tumblr_p7n8kqHMuD1uy4lhuo2_1280.png'),
		url('https://78.media.tumblr.com/5ecb41b654f4e8878f59445b948ede50/tumblr_p7n8on19cV1uy4lhuo1_1280.png'),
		url('https://78.media.tumblr.com/28bd9a2522fbf8981d680317ccbf4282/tumblr_p7n8kqHMuD1uy4lhuo3_1280.png');
	background-repeat: repeat-x;
	background-position: 
		0 20%,
		0 100%,
		0 50%,
		0 100%,
		0 0;
	background-size: 
		2500px,
		800px,
		500px 200px,
		1000px,
		400px 260px;
	animation: 50s para infinite linear;
	}

@keyframes para {
	100% {
		background-position: 
			-5000px 20%,
			-800px 95%,
			500px 50%,
			1000px 100%,
			400px 0;
        <style>
        """
st.markdown(project_background, unsafe_allow_html=True)

# Array to make CSV
intervals = np.array([[0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1]])
       
project_title = st.markdown(":green[Sustainability] Calculator :earth_americas:")
      
RV_title = st.number_input('Revenue Growth')

EB_title = st.number_input("EBITDA[*](https://www.bdc.ca/en/articles-tools/entrepreneur-toolkit/templates-business-guides/glossary/ebitda#:~:text=EBITDA%20is%20short%20for%20earnings,and%20ability%20to%20generate%20cash.)")

NE_title = st.number_input('Number of Employees')

Weight_title = st.number_input('Weight %')

EV_title = st.number_input('Enviornmental Score')

GoV_title = st.number_input('Government Score')

SS_title = st.number_input('Social Score')

ControS_title = st.number_input('Controversial Score')

SubmitBut = st.button("Calculate", type="primary")
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
    st.text(str(returntype))


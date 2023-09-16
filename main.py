import streamlit as st
import pandas as pd
import numpy as np
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

    predictData = loadtxt("test.csv", delimiter=',')
    predictRow = predictData[0:8]

    predictions = model.predict(inData)
    
    print(predictions[0])


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
values = []
       
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
    values.append(RV_title)
    values.append(EB_title)
    values.append(NE_title)
    values.append(Weight_title)
    values.append(EV_title)
    values.append(GoV_title)
    values.append(SS_title)
    values.append(ControS_title)
    arr = np.asarray(values)
    arr.tofile("test.csv",sep= ',')
    trainNetwork()



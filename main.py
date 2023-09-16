from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import streamlit as st

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

predictions = (model.predict(inData) > 0.5).astype(int)
for i in range(3):
 print('%s => %d (expected %d)' % (inData[i].tolist(), predictions[i], outData[i]))



 # UI Builder 

 with open('style.css') as f:
       st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
       
project_title = st.markdown(":green[Sustainability] Calculator :earth_americas:")
      
RV_title = st.text_input('Revenue Growth')

EB_title = st.text_input("EBITDA[*](https://www.bdc.ca/en/articles-tools/entrepreneur-toolkit/templates-business-guides/glossary/ebitda#:~:text=EBITDA%20is%20short%20for%20earnings,and%20ability%20to%20generate%20cash.)")

NE_title = st.text_input('Number of Employees')

Weight_title = st.text_input('Weight %')

EV_title = st.text_input('Enviornmental Score')

GoV_title = st.text_input('Government Score')

SS_title = st.text_input('Social Score')

ControS_title = st.text_input('Controversial Score')
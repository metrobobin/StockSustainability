from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

trainingData = loadtxt('./.venv/trunc_data.csv', delimiter=',')

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
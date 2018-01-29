from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from numpy import genfromtxt
from keras.models import model_from_json
from keras.optimizers import SGD


# fix random seed for reproducibility
np.random.seed(7)

# load pima indians dataset
#dataset = pd.read_csv("TRAIN_info_SMS.csv")
#test_dataset = pd.read_csv("DEV_info_SMS.csv")


# split into input (X) and output (Y) variables
# X = np.array(dataset[['Message']])
# Y = np.array(dataset[['Label']])

#f = open('glove/glove.6B.50d.txt','r')
#vecs = {}
#for line in f:
#    splitLine = line.split()
#    word = splitLine[0]
#    embedding = np.array([float(val) for val in splitLine[1:]])
#    vecs[word] = embedding

x = genfromtxt('xt.csv', delimiter=',')

#t_x = genfromtxt('DEV_info_SMS.csv', delimiter=',')



y = genfromtxt('yt.csv')
# print n
# print x
#print y
# print x.shape
#print y.shape
# create model
# model = Sequential()
# model.add(Dense(64, input_shape=(150,), activation='relu'))
# model.add(Dense(1, activation='softmax'))
# print model.summary()
# model.add(Dense(4, activation='sigmoid'))

# Compile model
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
# model.fit(x, y, epochs=150, batch_size=10)

# load pima indians dataset
# test_dataset = numpy.loadtxt("DEV_info_SMS.csv", delimiter=",")
# split into input (X) and output (Y) variables
# test_X = dataset[:,1:]
# test_Y = dataset[:,0]

# evaluate the model
json_file = open('model25.json','r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights('model25.h5')
sgd = SGD(lr=0.1, momentum=0.9, decay=0.0, nesterov=False)
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#t_y = y[:3000]
scores = model.evaluate(x, y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

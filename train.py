from keras.models import Sequential
from keras.layers import Dense, Dropout
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from numpy import genfromtxt
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

x = genfromtxt('x.csv', delimiter=',')
#t_x = genfromtxt('DEV_info_SMS.csv', delimiter=',')
# print len(x)


y = genfromtxt('y.csv', delimiter=',')
# print len(y)
# print n
# print x
#print y
# print x.shape
#print y.shape
# create model
model = Sequential()
# model.add(Dropout(0.2, input_shape=(150,)))
# model.add(Dense(512, activation='relu'))
# model.add(Dense(256, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))
model.add(Dense(150, input_shape=(150,), activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(256, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
print model.summary()
# model.add(Dense(4, activation='sigmoid'))
sgd = SGD(lr=0.1, momentum=0.9, decay=0.0, nesterov=False)
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(x, y, epochs=150, batch_size=10)

# load pima indians dataset
# test_dataset = numpy.loadtxt("DEV_info_SMS.csv", delimiter=",")
# split into input (X) and output (Y) variables
# test_X = dataset[:,1:]
# test_Y = dataset[:,0]

# evaluate the model
model_json = model.to_json()
with open("model25f.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model25f.h5")

#t_y = y[:3000]
scores = model.evaluate(x, y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

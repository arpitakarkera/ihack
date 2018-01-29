from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from numpy import genfromtxt
from keras.models import model_from_json
from keras.optimizers import SGD
import os

dir = os.listdir('test_mails')

np.random.seed(7)

model = 'model25f.csv'



def detect(y):
    if y<5.00000e-01:
        return "not spam"
    else:
        return "spam"

def predict_result(x):
    json_file = open('model25f.json','r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    model.load_weights('model25f.h5')
    sgd = SGD(lr=0.1, momentum=0.9, decay=0.0, nesterov=False)
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # print model.summary()
    # print model.predict(x)
    prediction = model.predict(x)
    detctecd = [detect(z) for z in prediction]
    n = len(prediction)
    # print n
    for i in range(n):
        print str(dir[i])+" : "+detctecd[i]
    print "spam count: "+str(detctecd.count("spam"))

x = np.loadtxt('xft2.csv',delimiter=',')
# print x
predict_result(x)

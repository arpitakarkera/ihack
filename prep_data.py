import numpy as np
import pandas as pd
import string
from itertools import izip_longest
import math

train_data_file = "test_final.csv"
test_data_file = "test_data.csv"
glove_file = "glove/glove.6B.50d.txt"

data = pd.read_csv(train_data_file)
# test_data = pd.read_csv(test_data_file)
glove = open(glove_file,'r')
# data = pd.concat([data,test_data])
print data
n = len(data.index)
y = data.label
data = data.replace(np.nan, '', regex=True)

word_vec = {}
for line in glove:
    splitLine = line.split()
    word = splitLine[0]
    # print word
    embedding = np.array([float(val) for val in splitLine[1:]])
    word_vec[word.lower()] = embedding

X = data[['subject','body','attachment']]
# print data.label
# y = data.label
# print y

replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
x = np.zeros((n,150))
for i in range(n):
    msg_subject = X.subject[i].translate(replace_punctuation).split()
    msg_body = X.body[i].translate(replace_punctuation).split()
    msg_attachment = X.attachment[i].translate(replace_punctuation).split()
    s_subject = np.zeros(50)
    s_body = np.zeros(50)
    s_attachment = np.zeros(50)
    c_subject = c_body = c_attachment = 0
    for word_subject, word_body, word_attachment in izip_longest(msg_subject,msg_body,msg_attachment):
        try:
            s_subject += word_vec[word_subject.lower()]
            c_subject += 1
        except:
            pass
        try:
            s_body += word_vec[word_body.lower()]
            c_body += 1
        except:
            pass
        try:
            s_attachment += word_vec[w]
            c_attachment += 1
        except:
            pass
    if c_subject!=0:
        s_subject = s_subject/c_subject
    if c_body!=0:
        s_body = s_body/c_body
    if c_attachment!=0:
        s_attachment = s_attachment/c_attachment
    x[i] = np.concatenate((s_subject, s_body, s_attachment))
np.savetxt("xft2.csv", x, delimiter=",")
# y.to_csv('yft.csv',index=False)

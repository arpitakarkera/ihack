import pandas as pd
from sklearn.utils import shuffle

ham = pd.read_csv('ham.csv')
ham2 = pd.read_csv('ham2.csv')
spam = pd.read_csv('spam.csv')

data = pd.concat([ham,ham2])
data = pd.concat([data,spam])
# print data.head()
data=data.sample(frac=1).reset_index(drop=True)
# print len(data.index)
# print data.head()
data[:16000].to_csv('train_data.csv',index=False)
data[16000:].to_csv('test_data.csv', index=False)

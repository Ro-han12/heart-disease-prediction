# -*- coding: utf-8 -*-
"""heart disease prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UpOzyumhblD9o2VKqGpBuAkNpftwUtf4
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data=pd.read_csv('/content/heart_disease_data.csv')
data.head()

data.info()

data.describe()

data.isnull().sum()

data['target'].value_counts()

"""sepreating dependent & independent

"""

x = data.drop(columns='target',axis=1)
y = data['target']

print(x)

print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

print(x_train)

print(x_test)

print(y_train)

print(y_test)

"""feature scaling"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

print(x_train)

print(x_test)

from sklearn.linear_model import LogisticRegression
regressor=LogisticRegression()
regressor.fit(x_train,y_train)

"""ACCURACY SCORE

"""

x_train_predict=regressor.predict(x_train)
training_data_accuracy=accuracy_score(x_train_predict,y_train)

print("accuracy on training data:",training_data_accuracy)

x_test_predict=regressor.predict(x_test)
test_data_accuracy=accuracy_score(x_test_predict,y_test)

print("accuracy on training data:",test_data_accuracy)

"""predicting"""

input_data=(41,0,1,130,204,0,0,172,0,1.4,2,0,2)
a=np.asarray(input_data)
a_new=a.reshape(1,-1)
prediction=regressor.predict(a_new)
print(prediction)
#1 has defect and 0 no defect
if (prediction[0]==0):
  print("person is safe!!!")
else:
  print("do have a check up")
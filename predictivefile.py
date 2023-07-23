# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
loaded_model=pickle.load(open('C:/Users/HP/Desktop/my projects/heart disease/trained_model .sav','rb'))
input_data=(41,0,1,130,204,0,0,172,0,1.4,2,0,2)
a=np.asarray(input_data)
a_new=a.reshape(1,-1)
prediction=loaded_model.predict(a_new)
print(prediction)
#1 has defect and 0 no defect
if (prediction[0]==0):
  print("person is safe!!!")
else:
  print("do have a check up")
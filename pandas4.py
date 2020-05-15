# -*- coding: utf-8 -*-
"""
Created on Fri May 15 02:55:09 2020

@author: tolao
"""

import numpy as np
import pandas as pd
'''
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
#print(ser)
print(ser.value_counts())
print(ser.value_counts().index[:2])'''
#print(ser.value_counts().values)
a=pd.Series([1,2,3,4])
print(a)
a[[True,False,True,False]]="vay be"
print(a)



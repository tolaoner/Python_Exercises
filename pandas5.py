# -*- coding: utf-8 -*-
"""
Created on Fri May 15 03:49:20 2020

@author: tolao
"""
#Bin the series ser into 10 equal deciles and replace the values with the bin name.
import numpy as np
import pandas as pd
ser = pd.Series(np.random.random(20))
print(ser)
a=pd.qcut(ser,[0,0.1,0.2,.3,.4,.5,.6,.7,.8,.9,1],labels=["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th"])
print(a)
######################################################################################

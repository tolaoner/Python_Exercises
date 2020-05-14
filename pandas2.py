import numpy as np
import pandas as pd
'''ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
ser3= ser1[~ser1.isin(ser2)]
ser4=ser2[~ser2.isin(ser1)]
ser_u=pd.Series(np.union1d(ser3,ser4))
print(ser_u)'''
ser = pd.Series(np.random.normal(10, 5, 25)) 
import numpy as np
import pandas as pd
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
print(ser1[~ser1.isin(ser2)])# isin returns a series of booleans indicating each element is in values
print(~ser1.isin(ser2))
ser3=pd.Series([True,True,False,False,False])
print(ser2[ser3])

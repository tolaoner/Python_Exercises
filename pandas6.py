#exercise 12,13,14,15,16,17
import numpy as np
import pandas as pd
'''12-----ser = pd.Series(np.random.randint(1, 10, 35))
ser_df=pd.DataFrame(ser.values.reshape(7,5))
print(ser_df)'''
'''13----ser = pd.Series(np.random.randint(1, 10, 7))
print(ser)
a=np.argwhere(ser % 3==0)
print(a)'''
'''ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
a=ser.take(pos)
print(a)'''
'''15---ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
a=ser1.append(ser2)#stack series vertically
print(a)
df=pd.concat([ser1,ser2],axis=1)
print(df)'''
'''16---ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])
a= [pd.Index(ser1).get_loc(i) for i in ser2]
print(a)'''
'''---17 truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)
a=np.mean((truth-pred)**2)
print(a)'''
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
ser1=pd.Series([i[0].upper()+i[1:] for i in ser])
a=ser.map(lambda x: x.title())
print(ser1)
print(a)

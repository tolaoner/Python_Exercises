import numpy as np
import pandas as pd
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
#takes the random int, and uses it as index to get a letter from the list
frequency_count=[]
print(ser.array)
for element in list('abcdefgh'):
    count=0
    for i in ser.array:
        if element==i:
            count+=1
    frequency_count.append(count)
print(frequency_count)
#below is site solution
print(ser.value_counts())
    

import pandas as pd
import numpy as np


df1 = pd.DataFrame([[3,5,7,12,4],
                   [57700,4,2,45,6],
                   [6,3,3,7,5]],columns=['a','b','c','d','e'])

#創造<3個標準差的篩選條件(各欄為各自基準)
def filter(data):
    threshold = 3 #與平均值距離>3個標準差
    mean = data.mean()
    std = data.std()
    z_score = (data-mean)/std
    y = np.abs(z_score) < threshold 
    return y

print(df1[filter(df1)])




            
    
    
import pandas as pd
import numpy as np

df1 = pd.DataFrame([[0,1,2,3,4],
                   [77,4,2,45,6],
                   [6,3,3,7,5]],columns=['01','02','03','04','05'])

print(df1)

print('------------------------------')
df = pd.DataFrame(np.arange(15).reshape(3,5),
columns=['a','b','c','d','e'])

df3 = df.stack

'''
print( df )
print( df['dd'] ) #使用名稱取一欄
print( df.iloc[1] ) #使用索引值取一列
print( df.iloc[:, 3]) #使用索引值取一欄
print( df.iloc[1, 2]) #使用索引值取一值
print( df.loc['b']) #使用索引名稱取一列
print( df.loc[:, 'dd']) #使用索引名稱取一欄
print( df.loc['c',
'dd']) #使用索引名稱取一值
print( df.iloc[:2, 2:] ) #使用索引值切片
print( df.loc['a':'c', 'cc':'ee']) #使用索引名稱切片
'''
import pandas as pd

dict1 = {'a':1, 'b':3, 'c':5}
df1 = pd.DataFrame(dict1, index=['i1'])
print( df1 )

dict2 = {'aa':{'a':1, 'b':3, 'c':5},
 'bb':{'a':2, 'b':4, 'c':6},
 'cc':{'a':'apple','b':'banana','c':'watermelon'}}
df2 = pd.DataFrame(dict2)
print( df2 )
print( df2['bb'] ) #注意顯示的 dtype
print( df2['cc'] ) #注意顯示的 dtype
print( df2.loc[['a','c'], ['cc','aa']] ) #跳取列與欄的資料
print( df2.iloc[[0, 2], [2, 0]] ) #跳取列與欄的資料
#print( df2.T ) # 資料列與欄翻轉
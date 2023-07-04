import pandas as pd

df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])
df3 = pd.DataFrame([['apple', 3.1], ['banana', 4.2]],columns=['fruit', 'dollar'])

df12 = pd.concat([df1, df2]) #concat相接
print( df12 )
df12.index = (0,1,2,3)

df13 = pd.concat([df1, df3], axis=1) #預設axis=0(縱向)
print( df13 )
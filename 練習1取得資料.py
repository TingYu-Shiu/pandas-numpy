import pandas as pd
s1 = pd.Series({'陳大':84,'丁二':74,'張三':85,'李四':95,'王五':79})
s2 = pd.Series({'陳大':88,'丁二':93,'張三':76,'李四':67,'王五':98})
s3 = pd.Series({'陳大':76,'丁二':89,'張三':97,'李四':99,'王五':86})
df = pd.DataFrame({'國文':s1,'英文':s2,'數學':s3})
print( df ) 
print('---------------')
print('丁二的數學成績:',df.iloc[1,2])
print('---------------')
print(df.loc[:,['國文','數學']])
print('---------------')
print(df.iloc[2:,:])
print('---------------')
print(df.iloc[[1,2,4],[1,0]])
print('---------------')
print(df)
import pandas as pd

s1 = pd.Series({'陳大':84,'丁二':74,'張三':85,'李四':95,'王五':79})
s2 = pd.Series({'陳大':88,'丁二':93,'張三':76,'李四':67,'王五':98})
s3 = pd.Series({'陳大':76,'丁二':89,'張三':97,'李四':99,'王五':86})
df1 = pd.DataFrame([s1, s2, s3])
print( df1 )


df1.index = ['國文','英文','數學']
print( df1 )


df2 = pd.DataFrame({'國文':s1,'英文':s2,'數學':s3})
print( df2)

'''
df2.columns = ['course1', 'course2', 'course3']
print( df2 )

df = df2.copy()

print( df.drop('陳大') )
print( df.drop(['陳大','張三','王五']) )
print( df.drop('course1', axis=1) )
# 如要真的從 df 刪除，需回存
df = df.drop('course1', axis=1)
print( df )

print( df.drop( df.index[1:4] ) )
print( df.drop( df.index[[0,2,4]] ) )
print( df.drop( df.columns[:2], axis=1 ) )
print( df.drop( df.columns[[0,2]], axis=1) )

df.index = ['陳大','丁二','張三','李四','王五']
df.columns = ['國文','英文','數學']
df = df.rename( columns={'英文':'Eng'}, index={'王五':'Wang'} )
print( df )
'''
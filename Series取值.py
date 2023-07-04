import pandas as pd

#取值建議用loc，e.g. s1.loc[-3:]

s1 = pd.Series([2,5,8,4,9])
s2 = pd.Series([2,5,8,4,9], index=['a','b','c','d','e'])

d1 = pd.date_range('20211008', periods=5, freq='B')
s3 = pd.Series(['This','is','a','cook','book'],index=d1)

# s3 =s3.str.replace('is','^') series 內若為字串要修改需要加上.str

s1.sort_values(ascending = False)
s1.sort_index(ascending = False)

s2.describe() #看基礎分析數據

s2.idxmax() #values最大值的index是多少
s2.idxmin()

s3.unique() #取不重複值
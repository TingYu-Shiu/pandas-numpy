import pandas as pd
import numpy as np


s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series(np.arange(5,10),index=['a','b','c','d','e'])
dict1 = {'aa':5,'bb':3,'cc':9}
s3 = pd.Series(dict1)


#pd.date_range(start=起始日期,end=結束日期,periods=天數個數,freq=個數)
#values取值，index查索引及類型，dtype查值的型態，size查詢個數

d1 = pd.date_range('20210928', '20211003')
d2 = pd.date_range('20210928',periods=5)
d3 = pd.date_range(end='20210928',periods=5)
d4 = pd.date_range('20210928', '20211010',periods=4)
d5 = pd.date_range('20210928',periods=5,freq='M')
s4 = pd.Series((7,44,3,5,2), index = d5)


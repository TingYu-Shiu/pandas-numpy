import pandas as pd
import matplotlib.pyplot as plt

data = [[9,    203674, 13.2, 18894,'北部'],
        [11.7, 180785, 12.3, 54894,'中部'],
        [10.1, 127802, 14.7, 18563,'北部'],
        [11.8, 28604,  14.9, 21963,'北部'],
        [13.2, 600,    13.1, 900 , '東部'],
        [6.9,  38071,  9.6,  3555 ,'北部'],
        [12.1, 35660,  10.6, 9005 ,'南部'],
        [12,   15000,  13,   12000,'中部'],
        [11.7, 48770,  9.1,  14370,'南部'],
        [9.84, 6100, 11.89, 8980 , '中部']]
indexs = ["三重市","台中市","台北一","台北二","台東市",
          "板橋區","高雄市","嘉義市","鳳山區","豐原區"]
cols = ["西瓜價","西瓜量","香瓜價","香瓜量","區域"]
df = pd.DataFrame( data, index=indexs, columns=cols)

'''
print(df[df['區域'].isin(['中部','南部'])])
print(df[df['香瓜量'].between(10000,20000)])
Series.between( 起始值, 結束值, inclusive='both')
inclusive 值可以是 both、neither、left、right

print( df[ ~df['區域'].isin(['中部','南部']) ])
篩出除了中部與南部以外的資料(~)

df.sum(numeric_only=True)
純粹數字才做加總

'''
x=df.groupby('區域')

for i in x:
    print(i)
    print('---------------------')

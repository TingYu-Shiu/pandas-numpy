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


plt.figure( figsize=(10,5), dpi=300)
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'

sa = df.groupby('區域')['西瓜量'].sum()
sb = df.groupby('區域')['香瓜量'].sum()

ex =[0.2,0,0,0]
lbl =['中部','北部','南部','東部']
co = ['r','y','c','g']

plt.subplot(1,2,1) 
plt.pie(sa,explode=ex,labels=lbl, colors=co, autopct='%.2f%%')
plt.subplot(1,2,2)
plt.pie(sb,explode=ex,labels=lbl, colors=co, autopct='%.2f%%')
plt.pie()
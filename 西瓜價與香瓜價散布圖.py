import pandas as pd
import numpy as np
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

x = df['西瓜量']/25
y = df['香瓜量']/25

plt.scatter(indexs, df['西瓜價'],label='西瓜價', s=x,alpha=0.5)
plt.scatter(indexs, df['香瓜價'],label='香瓜價', s=y,alpha=0.5)

plt.legend()
plt.grid()
plt.title('各市場西瓜價與香瓜價的散布圖', fontsize=20)
plt.xlabel('果菜批發市場', fontsize=16)
plt.ylabel('價格', fontsize=16)
plt.savefig('3-3chart2.png')


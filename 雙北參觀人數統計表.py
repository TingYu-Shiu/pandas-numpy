import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei' 
plt.rcParams["axes.unicode_minus"] = False 

x = np.arange(1,13) 
y1=[79083,60274,49402,41602,46242,48996,69326,123224,106496,87557,93850,76577]

y2=[73733,72060,52988,47805,54012,49366,52241,53002,54823,63465,44245,56821]

plt.xlabel('月份',fontsize=7)
plt.ylabel('參觀人次',fontsize=7)
plt.title('雙北107~109年度地方文物館每月參觀總人次統計表',fontsize=10)
plt.grid()


plt.plot(x,y1,label='臺北市',marker='o')
plt.plot(x,y2,label='新北市',marker='o')
plt.legend()
plt.show 
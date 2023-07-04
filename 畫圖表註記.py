import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'DFKai-SB'
''' (顯示中文)
plt.rcParams["axes.unicode_minus"] = False   (負號不見，需加載)
(可以是Microsoft JhengHei、mingliu、或 DFKai-SB)
'''
plt.figure( figsize=(10,5), dpi=300, facecolor='#dddddd', edgecolor='#333333', frameon=True, linewidth=5)

x = np.linspace(-10, 10, 11) #從-10到10均勻取11個數字
print( 'x=',x )
y = x**3 + 6*x**2 - 5*x + 10
print( 'y=',y)

plt.xlim(-7.5, 8) #指定x軸範圍
plt.ylim(-100,600) #指定y軸範圍
plt.xlabel('time(hour)') #指定x軸標籤
#plt.xticks((-10,-7.5,0,7.5,10),('差','略差','普通','良好','優良') )
plt.xticks(np.linspace(-20, 20, 7 ))
#用list指定標籤格及轉換成代表意義
plt.ylabel('Income') #指定y軸標籤
plt.title('Income by time',fontsize=20)#指定圖標籤
plt.plot(x, y, 'k-.o',label ='line1')


y1 = -x**3 + 3*x**2  - 4*x -7
plt.legend() #搭配label使用
plt.grid(color='g',lw=0.5,ls='--',alpha=0.75) #grid(格線),lw(線寬),ls(線樣式)),marker(標記),ms(標記大小),alpha(透明度)
#plt.show() :show在螢幕
plt.plot(x, y1, color='#ff34bc',ls=":",marker="o",label ='line2') #顏色,線(標記)樣式
plt.legend() #搭配label使用


plt.savefig('chart.png') #存成檔案

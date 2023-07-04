import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'
plt.rcParams["axes.unicode_minus"] = False


x = np.array([5,42,8,18,21,9]) #男
y = np.array([37,29,46,12,65,20]) #女
z = np.array(['女裝','男裝','童裝','皮件','配件','背包'])
u = np.array([1,2,3,4,5,6])
s1 = int(sum(x))
s2 = int(sum(y))
w = np.array([s1,s2])
v = x+y
'''
lbl = ['男','女']
plt.title('男女銷售件數占比')
plt.pie(w, labels=lbl, autopct='%.2f%%',)
plt.legend(loc='upper left')
'''

'''
plt.title('各類別銷售件數占比')
plt.pie(v, labels=z, autopct='%.2f%%',)
'''

plt.xticks([1,2,3,4,5,6],['女裝','男裝','童裝','皮件','配件','背包'])
plt.grid()
plt.xlabel('銷售類別')
plt.ylabel('銷售件數')

'''
plt.bar(u-0.25,x,width=0.4,label='男')
plt.bar(u+0.25,y,width=0.4,label='女')
plt.legend(fontsize=10)
'''
plt.title('零售業各項類別銷售件數')
plt.plot(u,x,label='男')
plt.plot(u,y,label='女')
plt.legend(fontsize=10)



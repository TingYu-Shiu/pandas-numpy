import matplotlib.pyplot as plt
plt.figure( figsize=[4,4], dpi=100,facecolor='#eeeeff', edgecolor='b',linewidth=1, frameon=True)


x = [1,3,5,7,9]
y1 = [5,3,8,6,9]
y2 = [2,6,8,3,4]

plt.subplot(2,1,1) # 可以寫成 plt.subplot(211)
plt.plot(x, y1, color='g')
plt.subplot(2,1,2)
plt.plot(x, y2, color='y')
plt.show()
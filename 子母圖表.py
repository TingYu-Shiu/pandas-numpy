import matplotlib.pyplot as plt

plt.figure( figsize=[4,4], dpi=100,facecolor='#eeeeff', edgecolor='b',linewidth=1, frameon=True)

x = [1,3,5,7,9]
y1 = [5,3,8,6,9]
y2 = [2,6,8,3,4]
plt.axes([0.01, 0.01, 0.96, 0.96])
#第一張(距左邊框多遠,距下邊框多遠,多寬,多高)
plt.plot(x, y1, color='g')
plt.axes([0.6, 0.1, 0.3, 0.2])
#第一張(距左邊框多遠,距下邊框多遠,多寬,多高)
plt.plot(x, y2, color='y')
plt.show()
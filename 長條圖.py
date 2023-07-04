import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'
plt.rcParams["axes.unicode_minus"] = False

x = np.array([1,3,5,7,9])
y1 = np.array([5,3,8,6,9])
y2 = np.array([8,7,3,1,2])

#plt.bar(x-0.4, y1)
#plt.bar(x+0.4, y2) 並排的長條圖

plt.bar(x, y1, label = '男性')
plt.bar(x, y2, bottom = y1, label='女性') #堆疊長條圖(由y1頂部開始排)

plt.legend()
plt.show()
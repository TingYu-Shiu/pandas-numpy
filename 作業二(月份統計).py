import numpy as np
import matplotlib.pyplot as plt


months=np.array(['Jun','Jul','Aug','Sep'])
counts=np.array([20,30,40,10])


plt.subplot(1,2,1)
plt.bar(months, counts)


plt.subplot(1,2,2)

keypoint=[0,0,0.1,0]
color=['yellowgreen','gold','lightskyblue','lightcoral']

plt.pie(counts,colors=color,labels=months,explode=keypoint,autopct='%.1F%%')

plt.axis('equal')
plt.savefig('chart.png')


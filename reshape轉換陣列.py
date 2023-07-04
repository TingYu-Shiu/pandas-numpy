import numpy as np


np1 = np.arange(12)
print("np1一維:\n",np1 )
np2 = np1.reshape(2,6)
print("np2二維:\n",np2 )
print("np2的轉置矩陣：\n",np2.T)


np3 = np.array([7,3,2,7,4,3,8,9,1,5,6,2]).reshape(2,6)
print("np3二維:\n",np3 )
np4 = np3.reshape(2,2,3)
print("np4三維:\n",np4)

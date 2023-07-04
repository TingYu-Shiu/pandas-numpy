import numpy as np


np1 = np.arange(5,30,3)
print("np1:\n",np1 )
print("np1[5]:",np1[5])
print("np1[1:-1]:",np1[1:-1])
print("np1[[3,8,1]]:",np1[[3,8,1]])
print("np1倒排：",np1[::-1])

np2 = np.arange(1,21).reshape(4,5)
print("np2:\n",np2 )
#print("np2[3,2]:",np2[3,2])
#print("np2[1:4,:3]:\n",np2[1:4,:3])
print("np2[[0,3,1],2:4]:\n",np2[[0,3,1],2:4])
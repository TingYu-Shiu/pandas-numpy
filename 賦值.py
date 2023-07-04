import numpy as np

np1 = np.arange(1,26).reshape(5,5)
print("np1:\n",np1 )
np2 = np1[3::-1,1:-1]
np3 = np1[3::-1,:1:-1]
print("np2:\n",np2 )
print("np3:\n",np3)

print("np2[2,2]:",np2[2,2] )
np2[2, 2] = 100
print("np2:\n",np2 )
print("np1:\n",np1 )
np3 = np1[3::-1, :1:-1].copy()
print("np3:\n",np3 )
print("np3[1,1]:",np3[1,1] )
np3[1] = 200
print("np3:\n",np3 )
print("np1:\n",np1 )

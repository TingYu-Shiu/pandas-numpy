import numpy as np

#seed = 12345
# np.random.RandomState(seed) = 將亂數規則固定

#np1 = np.random.RandomState(seed).randint(0,5,(5,4)) # 亂數 0-4 之間的值
#print("np1:\n",np1 )


np2 = np.random.randint(5, size=(2))
print("np2:\n",np2 )
np3 = np.random.randint(5, 10, size=(2,3)) # 亂數 5-9 之間的值
print("np3:\n",np3 )
np4 = np.random.choice(10,(5,2)) # 亂數 0-9 之間的值
print("np4:\n",np4 )
np5 = np.random.choice(range(1,50), (6,3), replace=True)
print("np5:\n",np5 )

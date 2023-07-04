import numpy as np

seed = 123

np1 = np.random.RandomState(seed).randint(5,16,size=15)
np2 =np.random.RandomState(seed).randint(5,15,size=15).reshape(3,5)

print("隨機正整數:",np1)
print("X矩陣內容：\n",np2,sep="")
print('最大：',np.max(np2))
print('最小:',np.min(np2))
print('總和：',np.sum(np2))

np3 = np2[np.ix_([0,2],[0,4]) ]
print("四個角落元素：\n",np3,sep="")

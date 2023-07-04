import numpy as np


np1 = np.arange(1,26).reshape(5,5)
print(np1)
print()

#練習1
print(np1[0:,3].reshape(5,1))
print()
#練習2
print(np1[2:4,[0,1,3,4]])
print()

#練習3
print(np1[1,[1,3]])
print(np1[3,[1,3]])
print(np1[3,[1,3]])
print(np1[[1,3],[1,3]])

'''
np2 = np.ix_([1,3],[1,3])
print(np2)

np3 = np1[np.ix_([1,3],[1,3]) ]
print(np3)
'''

import numpy as np

list1 = [5,6,2,8,1,2]

np1 = np.array(list1).reshape(2, 3)
print(np1)

np2 = np.array([23.5,23,34])
print(np2)

np3 = np.array( range(5,10) )
print(np3)

np4 = np.array([i*2 for i in range(5,60,10)])
print(np4)


np6 = np.array((range(5,60,10)))
print(np6)

np7 = np.array([5,3.25,14.3,6,8])
print(np7)

np8 = np.array([5,3.25,14.3,6,8], dtype = "int")
print(np8)
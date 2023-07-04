import numpy as np


np1 = np.array([[2,4,6],
                [7,8,9]])
print(np1)
print()


np2 = np.array([[[2,4,6,2],
                 [5,6,7,8],
                 [3,9,1,3]],
                [[2,45,2,3],
                 [32,64,3,-1]
                 ,[3,4,5,2]]])
print("np2:\n",np2 )
print()
print("np2 維度:", np2.ndim ) 
print("np2 形狀:", np2.shape ) 
print("np2 項目個數:", np2.size )
print("np2 型態:", np2.dtype )

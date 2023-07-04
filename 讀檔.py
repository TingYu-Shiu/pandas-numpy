import numpy as np
np1 = np.genfromtxt('abc.txt', delimiter=' ',encoding ='utf-8')
print( np1 )
print( np1.astype('int') )
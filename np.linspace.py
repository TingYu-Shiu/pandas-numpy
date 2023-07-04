import numpy as np


# 運用 np.linspace(起始值, 結束值, 建立項目數量) 來建立一維陣列
np1 = np.linspace(10, 19, 7)
print( 'np1:', np1 )

# 建立全部 0 組成的陣列
np2 = np.zeros( (5,2),dtype='int' )
print( 'np2:\n', np2)

# 建立全部 1 組成的陣列
np3 = np.ones( (6,) )
print( 'np3:', np3)

# 建立沒有初始化項目的陣列
np4 = np.empty( 8,dtype='int' )
print( 'np4:', np4)

np5 = np.eye(8,dtype='int')
print('np5:\n',np5)

np6 = np.full((2,3),8)
print('np6:\n',np6)
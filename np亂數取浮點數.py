import numpy as np

# 產生均勻分布之大於等於 0、小於 1 的亂數，參數個數決定維度
np1 = np.random.rand(5)
print("np1:\n",np1 )
np2 = np.random.rand(3, 3)
print("np2:\n",np2 )

# 產生常態分佈的亂數，參數個數決定維度
np3 = np.random.randn(3, 5)
print("np3:\n",np3 )

normal_array = np.random.normal(5,0.5,10) 
#產生平均數字為五，標準差為0.5內的數字


# 產生均勻分布之大於等於 0、小於 1 的亂數，但只放一個參數
np4 = np.random.random(5)
print("np4:\n",np4 )
np5 = np.random.random((3, 3))
print("np5:\n",np5 )
# np.random.random_sample()、0# np.random.sample()
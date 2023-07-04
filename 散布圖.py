import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1,20,size=20)
y = np.random.randint(1,100,size=20)
size= np.random.randint(1,1000,20)
plt.scatter(x,y,s=size, alpha=0.5)

z = np.random.randint(1,100,20)
plt.scatter(x,z,s=size, alpha=0.5)

plt.show()
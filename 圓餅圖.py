import matplotlib.pyplot as plt
import numpy as np

y = [7,4,3,9,5]
ex =[0.2,0,0,0,0]
lbl =['Python','C','C++','Java','JavaScript']
co = ['r','y','c','g','b']

plt.pie(y,explode=ex, labels=lbl, colors=co, autopct='%.2f%%', startangle=0, shadow=True, labeldistance=1.2, pctdistance=0.7)
plt.legend(loc ='lower right',fontsize=7)

plt.show

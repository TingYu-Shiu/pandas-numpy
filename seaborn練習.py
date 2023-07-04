import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set()

df = pd.read_csv('train.csv')

x=np.random.randn(100)
y=np.random.randn(100)

df_num = df.select_dtypes(include = ['float64','int64']) #只選數值相關型態

plt.figure(figsize=(15,10))
plt.subplot(2, 2,1)
sns.kdeplot((x,y),shade=True,cbar=True)
#sns.histplot(df['SalePrice'])
plt.subplot(2, 2,2)
sns.distplot(df['SalePrice'],bins=50,hist=True,kde=True)
plt.subplot(2, 2,3)
sns.kdeplot(df['SalePrice'],shade=True) 
#Kernel Density Estimation, KDE) 核密度估計
plt.subplot(2, 2,4)
sns.boxplot(x="OverallCond",y="SalePrice",data=df)


df_num.hist(figsize=(16,20), bins=50) #df直接匯出全部的圖


for i in range(0, len(df_num.columns), 5):
    sns.pairplot(data=df_num,x_vars=df_num.columns[i:i+5],y_vars=['SalePrice'])
    plt.savefig(str(i)+'.png')
    
sns.regplot(data=df_num,x='GrLivArea',y='SalePrice')  #有回歸線
    
df11 =df_num.corr() #corr相關係數
plt.figure(figsize=(12,10))

sns.heatmap(df11[(df11>=0.5)|(df11<=-0.4)],annot=True, vmax=1.0, vmin=-1.0,annot_kws={"size": 8},cmap='viridis')
#熱力圖
#https://blog.csdn.net/ztf312/article/details/102474190



plt.savefig('test.png')

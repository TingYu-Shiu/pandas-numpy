import pandas as pd

df = pd.read_csv("3-3read.csv")

x = df.groupby('居住縣市')['居住縣市'].count()
df1 = x.sort_values(ascending=False)
print(df1)

df3 = df.groupby('感染國家')['感染國家'].count()
print(df3.sort_values(ascending=False).head(5))

tpe = df[df['居住縣市'] == '台北市']
df4 = tpe.groupby('居住鄉鎮')['居住鄉鎮'].count()
print(df4)

print('發病日:',tpe['發病日'].max())
import pandas as pd
datas = [[75, 62, 85, 73, 60],
 [91, 53, 56, 63, 65],
 [71, 88, 51, 69, 87],
 [69, 53, 87, 74, 70]]

indexs = ["小林","小黃","小陳","小美"]
columns = ["國語","數學","英文","自然","社會"]

df = pd.DataFrame(datas, index=indexs, columns=columns )

print(df)
print('---------------')
print(df.tail(2))
print(df.iloc[-2:])
print('---------------')
print((df.iloc[:,-2]).sort_values(ascending=False))
df.iloc[1,2]=80
print(df.iloc[1,:])
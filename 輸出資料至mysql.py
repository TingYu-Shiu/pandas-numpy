import pandas as pd
import MySQLdb 

conn = MySQLdb.connect('Localhost','root','Qoo830204199483')
cursor = conn.cursor()
# Drop database if it already exist using execute() method.
cursor.execute("DROP DATABASE IF EXISTS lotto")
cursor.execute("CREATE DATABASE lotto")
conn.close()

conn1 = MySQLdb.connect('Localhost','root','Qoo830204199483',"lotto" )

url='https://www.taiwanlottery.com.tw/lotto/lotto649/history.aspx'

df = pd.read_html( url ) #讀html檔

colName = ['期別','開獎日','兌獎截止','銷售金額','獎金總額','獎號1','獎號2','獎號3','獎號4','獎號5','獎號6','特別號']
# 建立一個有欄位名稱，但資料是空的的 DataFrame
lotto = pd.DataFrame(columns=colName)


for d in df[2:-1]: #大樂透取內容
    data = []
    data.append(d.iloc[1,0])    #期別
    data.append(d.iloc[1,1])    #開獎日
    data.append(d.iloc[1,3])    #兌獎截止
    data.append(d.iloc[1,5])    #銷售金額
    data.append(d.iloc[1,7])    #獎金總額
    for i in range(2, 9):
        data.append( d.iloc[4, i] )
    print( data )
    
    dftemp = pd.DataFrame([data],columns=colName)
    lotto = pd.concat([lotto, dftemp])
    print('--------------------')
lotto.index =(0,1,2,3,4,5,6,7,8,9)

lotto.to_sql('大樂透數期中獎號', con=conn , index=False, if_exists='replace' ) 
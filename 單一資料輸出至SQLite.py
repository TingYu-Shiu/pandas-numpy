import pandas as pd
import sqlite3

conn = sqlite3.connect('中獎號碼.db')

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
    sql = 'Select * from 大樂透數期中獎號 where 期別="' + data[0] + '"'
    try:
        dfcheck = pd.read_sql(sql, conn) #確認是否有該表格存在
    except:
        dfcheck = pd.dataFrame(columns=colName) #建立一個DataFrame
    if len(dfcheck)==0:
        dftemp.to_sql('大樂透數期中獎號', conn, if_exists='append', index=False)

    print('--------------------')

conn.close()


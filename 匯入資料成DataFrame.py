import pandas as pd


url = 'https://od.cdc.gov.tw/eic/NHI_EnteroviralInfection.csv'
df = pd.read_csv( url ) #讀csv檔

url1= 'https://od.cdc.gov.tw/eic/NHI_EnteroviralInfection.json'
df1 = pd.read_json( url1 ) #讀json檔


url2= 'https://www.taiwanlottery.com.tw/lotto/lotto649/history.aspx'
df2 = pd.read_html( url2 ) #讀html檔

for d in df2[2:-1]: #大樂透取內容
    data = []
    data.append(d.iloc[1,0])    #期別
    data.append(d.iloc[1,1])    #開獎日
    data.append(d.iloc[1,3])    #兌獎截止
    data.append(d.iloc[1,5])    #銷售金額
    data.append(d.iloc[1,7])    #獎金總額
    for i in range(2, 9):
        data.append( d.iloc[4, i] )
    print( data )
    print('--------------------')
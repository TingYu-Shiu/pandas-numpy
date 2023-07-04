import sqlite3
import pandas as pd


conn = sqlite3.connect('中獎號碼.db')

df = pd.read_sql('Select * from 大樂透數期中獎號', conn, index_col='期別')
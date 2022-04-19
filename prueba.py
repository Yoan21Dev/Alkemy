from os import sep
import pandas as pd 
import io, requests
from decouple import config
from sqlalchemy import create_engine


engine = create_engine('postgresql://postgres:12345@localhost/holap')


with requests.Session() as s:
    r = s.get(config('CSV_URL_M'))
    decode_content = r.content.decode('utf-8')  
    df = pd.read_csv(io.StringIO(decode_content),sep= ',', index_col=0)
    # df_cod = df[['Cod_Loc','IdProvincia','IdDepartamento']]
    df.to_sql('users', con=engine, if_exists='append')
    # db = engine.execute("SELECT * FROM users").fetchall()
    # print (db)
# ruta = 'C:\Users\YARM\Desktop\Alkemy\Dates\Biblioteca\2022-abril\Biblioteca -2022-04-04\Biblioteca.csv'
# df = pd.read_csv(f'{ruta}',sep=',',names=['col1','col2'], encoding='utf-8')
# print(df)

   
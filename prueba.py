from os import sep
import pandas as pd 
import io, requests
from decouple import config
from sqlalchemy import create_engine, values


engine = create_engine('postgresql://postgres:12345@localhost/holap')

none = 'Desconocido'

with requests.Session() as s:
    r = s.get(config('CSV_URL_M'))
    decode_content = r.content.decode('utf-8')  
    df = pd.read_csv(io.StringIO(decode_content),sep= ',', )
    value_defaul = {'Web':'desconocido','Mail':'desconocido','telefono':'desconocido','cod_area':'desconocido'}
    values_df = (df.fillna(value = value_defaul))
    df_cod = values_df[['Cod_Loc','IdProvincia','IdDepartamento','categoria','provincia','localidad','nombre','cod_area','telefono','Mail','Web']]
    print(df_cod) 
   

    # db = engine.execute("SELECT * FROM users").fetchall()
   
    # print (db)
# ruta = 'C:\Users\YARM\Desktop\Alkemy\Dates\Biblioteca\2022-abril\Biblioteca -2022-04-04\Biblioteca.csv'
# df = pd.read_csv(f'{ruta}',sep=',',names=['col1','col2'], encoding='utf-8')
# print(df)





# def dates_Col(data) :
#     with requests.Session() as s:
#         r = s.get(data)
#         decode_content = r.content.decode('utf-8')  
#         df = pd.read_csv(io.StringIO(decode_content),sep= ',', )
#         df_cod = df[['Cod_Loc','IdProvincia','IdDepartamento','categoria','provincia','localidad','nombre','cod_area','telefono','Mail','Web']]
#         print(df_cod)


# dates_Col(config('CSV_URL_M'))
from datetime import date
from urllib.error import HTTPError as Error
import pandas as pd 
import io,requests,os.path,os,arrow
from decouple import config
import logging


data1 = config("CSV_URL_M")
data2 = config("CSV_URL_B")
data3 = config("CSV_URL_C")



def log_info ():
    logging.basicConfig(
        filename='%slog' % __file__[:-2],
        filemode='w'
    )
    return



def get_data_local(data, data_name): 
    with requests.Session() as s:
        try:
            r = s.get(data)
            decode_content = r.content.decode('utf-8')  
            df = pd.read_csv(io.StringIO(decode_content),index_col=0)
            today = date.today()
            month = arrow.utcnow().format('MMMM', locale='es')     
            directorio=(f'Dates\\{data_name}\\{today.year}-{month}\\{data_name}-{today}')
            os.makedirs(directorio,exist_ok=True)
            df.to_csv(f'{directorio}/{data_name}.csv')
        except Error:
            
            print({Error})
    return print('finish')


def get_remote_data(data):
    with requests.Session() as s:
        try:
            r = s.get(data)
            decode_content = r.content.decode("utf-8")
            df1 = pd.read_csv(
                io.StringIO(decode_content),
                sep=",",
            )
            return df1
        except Error:
            print({Error})

dates = pd.concat(
[get_remote_data(data1), get_remote_data(data2), get_remote_data(data3)]
)

value_defaul = {
"Web": "desconocido",
"Mail": "desconocido",
"provincia": "desconocido",
"localidad": "desconocido",
"nombre": "desconocido",
"categoria": "desconocido",
"telefono": "desconocido",
"Domicilio": "desconocido",
"cod_area": "desconocido",
}
values_df = dates.fillna( value = value_defaul)
df_cod = values_df[
[
    "Cod_Loc",
    "Domicilio",
    "IdProvincia",
    "IdDepartamento",
    "categoria",
    "provincia",
    "localidad",
    "nombre",
    "cod_area",
    "telefono",
    "Mail",
    "Web",
]
]
uniques = df_cod.groupby(['IdProvincia','provincia']).size().reset_index(name='count')

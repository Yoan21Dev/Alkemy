from os import sep
from unicodedata import category
import pandas as pd 
import io, requests
from decouple import config
from sqlalchemy import create_engine, values
from sqlalchemy.dialects.postgresql import insert
import src.models.data as bd
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://postgres:12345@localhost/efe')

Session = sessionmaker(engine)
session = Session()


with requests.Session() as s:
    r = s.get(config('CSV_URL_m'))
    decode_content = r.content.decode('utf-8')  
    df = pd.read_csv(io.StringIO(decode_content),sep= ',' )
    value_new = df.assign(domicilio='none')
    value_defaul = {'Web':'desconocido','Mail':'desconocido','telefono':'desconocido','cod_area':'desconocido','domicilio':'desconocido'}
    values_df = (value_new.fillna(value = value_defaul) )
    df_cod = values_df[['Cod_Loc','IdProvincia','IdDepartamento','categoria','provincia','localidad','nombre','cod_area','telefono','Mail','Web','domicilio']]
    for row in df_cod.itertuples():
        conn = engine.connect()
        god = bd.Producto( id_provincia=row.IdProvincia, id_departamento=row.IdDepartamento, category=row.categoria,provincia= row.provincia, localidad=row.localidad, nombre=row.nombre, codigo_postal = row.cod_area,numero_de_telefono=row.telefono,correo = row.Mail, web = row.Web, domicilio = row.domicilio )
        session.add(god)
        session.commit()

# def dates_Col(data) :
#     with requests.Session() as s:
#         r = s.get(data)
#         decode_content = r.content.decode('utf-8')  
#         df = pd.read_csv(io.StringIO(decode_content),sep= ',', )
#         df_cod = df[['Cod_Loc','IdProvincia','IdDepartamento','categoria','provincia','localidad','nombre','cod_area','telefono','Mail','Web']]
#         print(df_cod)


# dates_Col(config('CSV_URL_M'))
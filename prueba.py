from datetime import date
from os import sep
from unicodedata import category
import pandas as pd
import io, requests
from decouple import config
from sqlalchemy import create_engine, values
from sqlalchemy.dialects.postgresql import insert
import src.models.data as bd
from sqlalchemy.orm import sessionmaker

from urllib.error import HTTPError as Error

engine = create_engine("postgresql://postgres:12345@localhost/efe")

Session = sessionmaker(engine)
session = Session()


def get_remote_data(data):
    with requests.Session() as s:
        try:
            r1 = s.get(data)
            decode_content1 = r1.content.decode("utf-8")
            df1 = pd.read_csv(
                io.StringIO(decode_content1),
                sep=",",
            )
            return df1
        except Error:
            print({Error})


data1 = config("CSV_URL_M")
data2 = config("CSV_URL_B")
data3 = config("CSV_URL_C")

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
values_df = dates.fillna(value=value_defaul)
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
print(df_cod)

for row in df_cod.itertuples():
    conn = engine.connect()
    god = bd.info_documents(
        id_provincia=row.IdProvincia,
        id_departamento=row.IdDepartamento,
        category=row.categoria,
        provincia=row.provincia,
        localidad=row.localidad,
        nombre=row.nombre,
        codigo_postal=row.cod_area,
        numero_de_telefono=row.telefono,
        correo=row.Mail,
        web=row.Web,
        domicilio=row.Domicilio,
    )
    session.add(god)
    session.commit()

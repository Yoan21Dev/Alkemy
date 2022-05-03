from distutils.command.config import config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import src.models.data as models
import src.controller.Get_Data as df
import db


def queries():
    for row in df.df_cod.itertuples():
        god = models.info_documents(
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
        db.session.add(god)
        db.session.commit()
       

# # select * from users;
# users = session.query(User.id, User.username, User.email, User.create_at).filter(
#     User.id >= 2
# )

# for use in users :
#     print(use)
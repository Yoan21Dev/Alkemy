from distutils.command.config import config
import logging
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import src.models.models_data as models
import src.controller.Get_Data as df
import db


def queries():
    try:
        for row in df.df_cod.itertuples():
            God = models.info_documents(
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
            db.session.add(God)
            db.session.commit()
        for row in  df.uniques.itertuples():
            Pro = models.provincia( id_provincia = row.IdProvincia, name_provincia = row.provincia   
            ) 
            db.session.add(Pro)
            db.session.commit()

    except Exception as error :
        logging.error(f'error en models{error}')
        print (error)
# # select * from users;
# users = session.query(User.id, User.username, User.email, User.create_at).filter(
#     User.id >= 2
# )

# for use in users :
#     print(use)
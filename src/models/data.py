from datetime import datetime
from enum import unique
from unicodedata import category
from sqlalchemy.dialects import postgresql
from sqlalchemy.schema import CreateTable
from sqlalchemy import Column, Integer, String, DateTime,Float
import db

# class User(db.Base):

#     __tablename__ = 'Date'
#     id = Column(Integer(), primary_key=True)
#     id_provincia = Column(Integer())
#     id_departamento = Column(Integer(),) 
#     category = Column(String(), nullable=False)
#     provincia = Column(String(), nullable=False)
#     localidad = Column(String(),nullable= False)
#     nombre = Column(String(), nullable = False)
#     domicilio = Column(String(), nullable= False)
#     codigo_postal = Column(Integer(), nullable = False)
#     numero_de_telefono = Column(Integer(), nullable = False)
#     # correo = Column(string(),nullable = False)
#     web = Column (String(),nullable= False)
#     update_at = Column(DateTime(), default=datetime.now())
#     create_at = Column(DateTime(), default=datetime.now())
#     def __str__(self):
#         return self.category

class Producto(db.Base):
    __tablename__ = 'prueba'

    id = Column(Integer(), primary_key=True)
    id_provincia = Column(Integer())
    id_departamento = Column(Integer(),) 
    category = Column(String(), )
    provincia = Column(String(), )
    localidad = Column(String(),)
    nombre = Column(String(), )
    domicilio = Column(String(), )
    codigo_postal = Column(String(), )
    numero_de_telefono = Column(String(), )
    correo = Column(String(),)
    web = Column (String(),)
    update_at = Column(DateTime(), default=datetime.now())
    create_at = Column(DateTime(), default=datetime.now())
    def __str__(self):
        return self.id_provincia,self.category



   
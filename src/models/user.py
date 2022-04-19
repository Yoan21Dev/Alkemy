from datetime import datetime
import string
from unicodedata import category
from numpy import integer

from sqlalchemy import Column, Integer, String, DateTime,Float
import db_db as db



# class User(db.Base):

#     __tablename__ = 'users'
#     id = Column(Integer(), primary_key=True)
#     id_provincia = Column(Integer(), primary_key=True)
#     id_departamento = Column(Integer(), primary_key=True) 
#     category = Column(String(), nullable=False)
#     provincia = Column(String(), nullable=False)
#     localidad = Column(String(),nullable= False)
#     nombre = Column(String(), nullable = False)
#     domicilio = Column(String(), nullable= False)
#     codigo_postal = Column(integer(), nullable = False)
#     numero_de_telefono = Column(integer(), nullable = False)
#     mail = Column(string(), nullable = False)
#     web = Column (String(),nullable= False)
#     create_at = Column(DateTime(), default=datetime.now())
 
class Producto(db.Base):
    __tablename__ = 'producto'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def __repr__(self):
        return f'Producto({self.nombre}, {self.precio})'
    def __str__(self):
        return self.nombre



    # def __str__(self):
    #     return self.username
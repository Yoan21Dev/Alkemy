from datetime import datetime
from enum import unique
import string
from unicodedata import category
from sqlalchemy import Column, Integer, String, DateTime,Float
import db

class User(db.Base):

    __tablename__ = 'Date'
    id = Column(Integer(), primary_key=True)
    id_provincia = Column(Integer(), primary_key=True)
    id_departamento = Column(Integer(), unique=True) 
    category = Column(String(), nullable=False)
    provincia = Column(String(), nullable=False)
    localidad = Column(String(),nullable= False)
    nombre = Column(String(), nullable = False)
    domicilio = Column(String(), nullable= False)
    codigo_postal = Column(Integer(), nullable = False)
    numero_de_telefono = Column(Integer(), nullable = False)
    # correo = Column(string(),nullable = False)
    web = Column (String(),nullable= False)
    update_at = Column(DateTime(), default=datetime.now())
    create_at = Column(DateTime(), default=datetime.now())
    def __str__(self):
        return self.category,self.correo
 
class Producto(db.Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    create_at = Column(DateTime(), default=datetime.now())
   
    # def __init__(self, nombre, precio):
    #     self.nombre = nombre
    #     self.precio = precio

    # def __repr__(self):
    #     return f'Producto({self.nombre}, {self.precio})'

    def __str__(self):
        return self.nombre



   
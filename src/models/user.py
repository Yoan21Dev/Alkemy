from datetime import datetime
import string
from unicodedata import category
from numpy import integer

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class User(Base):

    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    id_provincia = Column(Integer(), primary_key=True)
    id_departamento = Column(Integer(), primary_key=True) 
    category = Column(String(), nullable=False)
    provincia = Column(String(), nullable=False)
    localidad = Column(String(),nullable= False)
    nombre = Column(String(), nullable = False)
    domicilio = Column(String(), nullable= False)
    codigo_postal = Column(integer(), nullable = False)
    numero_de_telefono = Column(integer(), nullable = False)
    mail = Column(string(), nullable = False)
    web = Column (String(),nullable= False)


    username = Column(String(50), nullable=False, unique = True)
    email = Column(String(50), nullable=False, unique=True)
    create_at = Column(DateTime(), default=datetime.now())
 
    def __str__(self):
        return self.username
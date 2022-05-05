from datetime import datetime
from enum import unique
from unicodedata import category
from sqlalchemy.dialects import postgresql
from sqlalchemy.schema import CreateTable
from sqlalchemy import Column, Integer, String, DateTime,Float
import db

class info_documents(db.Base):
    __tablename__ = 'datos'
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
   

class provincia(db.Base):
        __tablename__='provincias'
        id = Column(Integer(),primary_key = True)
        id_provincia = Column(String(),)
        name_provincia = Column(String(),)
        def __str__(self):
            return self.name_provincia

class total_record(db.Base):
        __tablename__='total_records'
        id =Column(Integer(),primary_key = True)
        categorias_totals = Column(Integer())
        fuentes_totals = Column(Integer())
        provincia_categoria_totals = Column(Integer())

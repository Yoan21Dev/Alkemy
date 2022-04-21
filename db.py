from sqlalchemy import create_engine, false, true,text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

engine = create_engine('{}://postgres:12345@localhost/postgres'.format(config('DB_ENGINE')))

Session = sessionmaker(engine)

session = Session()

Base = declarative_base() 


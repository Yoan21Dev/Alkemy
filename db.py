from sqlalchemy import create_engine, false, true,text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

Host = config('DB_HOST')
E1 =  config('DB_ENGINE')
E2 = config('DB_USER')
E3 = config('DB_PASSWORD')
E4 = config('DB_NAME')
E5 = config('DB_PORT')
engine = create_engine(f'{E1}://{E2}:{E3}@{Host}:{E5}/{E4}')

Session = sessionmaker(engine)

session = Session()

Base = declarative_base() 


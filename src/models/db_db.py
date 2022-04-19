from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:12345@localhost/example')

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()
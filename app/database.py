from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqLalchemy.orm import sessionmaker



SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Mollokapi1@localhost/fastapi"

engine= create_engine(SQLALCHEMY_DATABASE_URL)

Sessionlocal = sessionmaker(autocommit =False, autoflush= False, bind= engine)

Base = declarative_base()
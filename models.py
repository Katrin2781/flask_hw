import os
from atexit import register
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, String, Text, DateTime, Column, func


PG_USER = os.getenv('PG_USER', 'app')
PG_PASSWORD = os.getenv('PG_PASSWORD', '1234')
PG_DB = os.getenv('PG_DB', 'adverts_db')
PG_HOST = os.getenv('PG_HOST', '127.0.0.1')
PG_PORT = os.getenv('PG_PORT', 5431)

PG_DSN = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}'
engine = create_engine(PG_DSN)

register(engine.dispose)

Session = sessionmaker(bind=engine)
Base = declarative_base(bind=engine)

class Adverts(Base):
    __tablename__ = 'app_adverts'

    id = Column(Integer, primary_key=True)
    title_advert = Column(String, nullable=False, unique=True, index=True)
    description = Column(Text, nullable=False)
    create_date = Column(DateTime, server_default=func.now())
    user = Column(String, nullable=False, unique=True, index=True)


Base.metadata.create_all()
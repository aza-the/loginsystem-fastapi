import asyncio
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine


SQLALCHEMY_DATABASE_URL = 'postgresql://user:password@postgresserver/db'

#Create async engine for interaction with db
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, future=True, echo=True)

# async_session = e

Base = declarative_base()
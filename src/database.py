from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

from utils import DATABASE_URL


Base = declarative_base()

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

new_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    db = new_session()
    Base.metadata.create_all(bind=engine)
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(init_db)]

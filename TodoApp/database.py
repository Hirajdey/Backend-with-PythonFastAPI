from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path

# SQLite3 DB
# _DB_PATH = (Path(__file__).resolve().parent / "todosapp.db").as_posix()
# SQLALCHEMY_DATABASE_URL = f"sqlite:///{_DB_PATH}"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# PostgresSQL DB
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:123456@localhost:5432/TodoApplicationDatabase'


SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:123456@127.0.0.1:3306/TodoApplicationDatabase'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()













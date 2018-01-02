from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/raw_ta')

db_session = scoped_session(sessionmaker(autocommit=False,
                                autoflush=False,
                                bind=engine))

Base.query = db_session.query_property()
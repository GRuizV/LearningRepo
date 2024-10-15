from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from decouple import config

#DATABASE CONSTANTS
db_user = config('DB_USER')
db_pwd = config('DB_PASSWORD')
db_name = config('DB_NAME')

#DATABASE CREATION
url = f"postgresql://{db_user}:{db_pwd}@localhost/{db_name}"

engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

#DATABASE DEFINITION
class Conversation(Base):

    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String)
    message = Column(String)
    response = Column(String)


# Execution
Base.metadata.create_all(engine)











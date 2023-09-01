from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

path = "mysql+mysqldb://root:Speedy4life@localhost:3306/manueldb"

database = create_engine(path)

Session = sessionmaker(bind=database)
session = Session()
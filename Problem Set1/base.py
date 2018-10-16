from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import getpass

# Create an engine to the census database
pswd = getpass.getpass("Please enter your password:")
database = input("Please enter the database:")
db = "@localhost:3306/" + database

engine = create_engine("mysql+pymysql://root:"+ pswd + db)
Session = sessionmaker(bind=engine)

Base = declarative_base()

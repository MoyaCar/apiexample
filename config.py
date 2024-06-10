from sqlalchemy import create_engine
# read from .env file
import os
from dotenv import load_dotenv
load_dotenv()


user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_NAME')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
print(user, password, database, host, port)
engine = create_engine(
    f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}'
)

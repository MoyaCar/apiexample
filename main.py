from sqlalchemy.orm import Session
from config import engine
from db_creation import create_databases, create_entries
from models.system import System, Model, Owner
from fastapi import FastAPI
from sqlalchemy import text


app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Hello World'}

@app.get('/create-db')
def create_db():
    create_databases()
    with Session(engine) as session:
        #show tables
        result = session.execute(text('SHOW TABLES from globant_challenge'))
        tables = result.fetchall()
        print(tables)
    return {'message': 'Databases created'}

@app.get('/populate-databases')
def populate_databases():

    creation = create_entries()
    if creation != True:
        return creation
    with Session(engine) as session:
        query = session.query(System.system_id, Model.battery_size).join(Model).limit(2).all()

    system_with_bz = [
        {
            'system_id': element[0],
            'battery_size': element[1]
        } for element in query
    ]
    return system_with_bz

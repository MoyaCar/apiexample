from sqlalchemy.orm import Session
from models.system import System, Model, Owner, Base
from config import engine

def create_databases():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print('Databases created')

def create_entries():
    Owners = [
    Owner(name='John', last_name='Doe'),
    Owner(name='Jane', last_name='Doe'),
    Owner(name='John', last_name='Smith'),
    Owner(name='Jane', last_name='Smith')
    ]

    Models = [
        Model(model_id='HB300', battery_size=1000, manufacturer='Phanasonic'),
        Model(model_id='HB400', battery_size=2000, manufacturer='Phanasonic'),
        Model(model_id='HB301', battery_size=3000, manufacturer='Tesla'),
        Model(model_id='HB401', battery_size=4000, manufacturer='Tesla')
    ]

    Systems = [
        System(system_id='C4001', model_id='HB300', status='Active', owner_id=1),
        System(system_id='C4002', model_id='HB400', status='Active', owner_id=2),
        System(system_id='C4003', model_id='HB301', status='Inactive', owner_id=3),
        System(system_id='C4004', model_id='HB401', status='Inactive', owner_id=4)
    ]
    with Session(engine) as session:
        try:
            for owner in Owners:
                session.add(owner)
            for model in Models:
                session.add(model)
            for system in Systems:
                session.add(system)
            session.commit()
        except:
            session.rollback()
            return {'message': 'Duplicate entries'}

    print('Entries created')
    return True
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class Base(DeclarativeBase):
    pass

class System(Base):
    __tablename__ = 'systems'
    system_id = Column(String(50), primary_key=True, unique=True, nullable=False)
    model_id = Column(String(50), ForeignKey('models.model_id'), nullable=False)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    owner_id = Column(Integer, ForeignKey('owners.owner_id'), nullable=False)

    def __init__(self, system_id, model_id, status, owner_id):
        self.system_id = system_id
        self.model_id = model_id
        self.status = status
        self.owner_id = owner_id

    def __str__(self):
        return f'{self.system_id} - {self.model_id} - {self.status} - {self.created_at} - {self.owner_id}'

class Model(Base):
    __tablename__ = 'models'
    model_id = Column(String(50), primary_key=True, unique=True, nullable=False)
    battery_size = Column(Integer, nullable=False)
    manufacturer = Column(String(50), nullable=False)

    def __init__(self, model_id, battery_size, manufacturer):
        self.model_id = model_id
        self.battery_size = battery_size
        self.manufacturer = manufacturer

    def __str__(self):
        return f'{self.model_id} - {self.battery_size} - {self.manufacturer}'

class Owner(Base):
    __tablename__ = 'owners'
    owner_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f'{self.owner_id} - {self.name} - {self.last_name}'

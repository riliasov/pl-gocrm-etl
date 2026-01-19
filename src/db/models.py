from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    alias = Column(String)
    
class Center(Base):
    __tablename__ = 'centers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    city_id = Column(Integer, ForeignKey('cities.id'))
    
class Lead(Base):
    __tablename__ = 'leads'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fio = Column(String)
    phone = Column(String)
    status = Column(String)
    center_id = Column(Integer, ForeignKey('centers.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    comment = Column(Text)

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    fio = Column(String)
    name = Column(String)
    phone = Column(String)
    birthday = Column(String)
    
class SyncLog(Base):
    __tablename__ = 'sync_log'
    id = Column(Integer, primary_key=True)
    entity_name = Column(String)
    last_sync = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String)
    message = Column(Text)

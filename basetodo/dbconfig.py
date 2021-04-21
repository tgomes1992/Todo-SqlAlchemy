import sqlite3
from sqlalchemy import Column,Boolean, Integer, String, ForeignKey, Table , Float ,  Date , DateTime , create_engine
from sqlalchemy.orm import relationship, backref , sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd

Base = declarative_base()
engine = create_engine('sqlite:///todo.db')
conn  = engine.connect()

#support tables



class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    atividade = relationship('Atividade')

    def __repr__(self):
        return f"{self.id}-{self.nome}"
    
class Atividade(Base):
    __tablename__ = "atividades"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    status  = Column(Boolean)
    categoria = Column(Integer,ForeignKey("categorias.id"))
    
    def __repr__(self):
        return f'{self.id}-{self.nome}'

#main tables

# utilizado para criar um outro banco
#Base.metadata.create_all(engine)
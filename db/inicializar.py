from sqlmodel import SQLModel
from db.conexion import db

def crearTablas():
    SQLModel.metadata.create_all(db)
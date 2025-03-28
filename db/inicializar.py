from sqlmodel import SQLModel
from db.conexion import db
from db.modelos import Clientes, Pedidos, Productos, ProductosEnPedidos

def crearTablas():
    SQLModel.metadata.create_all(db)
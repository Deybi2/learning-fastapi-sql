from sqlmodel import Session, select
from db.conexion import db
from db.modelos import Pedidos

def listar_pedidos(cliente_id: str):
    with Session(db) as sesion:
        pedidos = sesion.exec(select(Pedidos).where(Pedidos.cliente_id == cliente_id)).all()
        return [{"order_id": pedido.id, "status": pedido.estado, "created_at": pedido.create_at.isoformat()} for pedido in pedidos]
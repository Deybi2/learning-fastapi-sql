from sqlmodel import Session, select
from db.conexion import db
from db.modelos import Pedidos
from fastapi import HTTPException

def consultar_estado_pedido(order_id: str, cliente_id: str):
    with Session(db) as sesion:
        pedido = sesion.exec(select(Pedidos).where(Pedidos.id == order_id, Pedidos.cliente_id == cliente_id)).first()
        if not pedido:
            raise HTTPException(status_code=404, detail="Pedido no encontrado o no pertenece al cliente.")
        return {"order_id": pedido.id, "status": pedido.estado}
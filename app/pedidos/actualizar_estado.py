from pydantic import BaseModel
from sqlmodel import Session, update, select
from db.conexion import db
from db.modelos import Pedidos
from fastapi import HTTPException

class EstadoPedido(BaseModel):
    estado: str

def actualizar_estado_pedido(order_id: str, estado_pedido: EstadoPedido, cliente_id: str):
    with Session(db) as sesion:
        pedido = sesion.exec(select(Pedidos).where(Pedidos.id == order_id, Pedidos.cliente_id == cliente_id)).first()
        if not pedido:
            raise HTTPException(status_code=404, detail="Pedido no encontrado o no pertenece al cliente.")
        
        pedido.estado = estado_pedido.estado
        sesion.add(pedido)
        sesion.commit()
        return {"order_id": pedido.id, "status": pedido.estado}
from pydantic import BaseModel
from sqlmodel import Session, select, update
from db.modelos import Productos, Pedidos, ProductosEnPedidos   
from db.conexion import db
from uuid import uuid4
from datetime import datetime

class ProductosEnPedidoRegistrar(BaseModel):
    producto_id: str
    cantidad: int

class PedidoARegistrar(BaseModel):
    cliente_id: str
    productos: list[ProductosEnPedidoRegistrar]

def registrar(pedidoARegistrar: PedidoARegistrar):
    with Session(db) as sesion:
        for producto in pedidoARegistrar.productos:
            producto_existente = sesion.exec(select(Productos).where(Productos.id == producto.producto_id)).first()
            if not producto_existente:
                raise ValueError(f"El producto {producto.producto_id} no existe.")

        pedido = Pedidos(cliente_id=pedidoARegistrar.cliente_id, create_at=datetime.now())
        sesion.add(pedido)

        for producto in pedidoARegistrar.productos:
            sesion.add(
                ProductosEnPedidos(
                    pedido_id=pedido.id,
                    producto_id=producto.producto_id,
                    cantidad=producto.cantidad
                )
            )

        sesion.commit()
        sesion.refresh(pedido)
    return {
        "order_id": pedido.id,
        "status": "Pendiente",
        "created_at": pedido.create_at.isoformat()
    }
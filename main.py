from db.modelos import Clientes, Productos
from db.inicializar import crearTablas
from db.conexion import db
from app.clientes.registrar import registrar as registrarNuevoCliente
from app.productos.registrar import registrar as registrarNuevoProducto
from app.pedidos.registrar import PedidoARegistrar, registrar as registrarNuevoPedido
from app.clientes.consultar_pedido import consultarPedidos
from app.clientes.consultar_pedido_especifico import consultarPedidoEspecifico
from app.clientes.actualizar_estado_de_pedido import actualizarEstadoPedido, EstadoPedido
from app.pedidos.consultar_estado import consultar_estado_pedido
from app.pedidos.actualizar_estado import actualizar_estado_pedido, EstadoPedido
from app.pedidos.listar_pedidos import listar_pedidos
from fastapi import FastAPI, Depends


app = FastAPI()

@app.on_event("startup")
def startup_event():
    crearTablas()

@app.get("/api/saludo")
def read_root():
    return {"Hello": "World"}

@app.post("/api/v1/clientes")
def post_clientes(cliente: Clientes):
    return registrarNuevoCliente(cliente)

@app.post("/api/v1/productos")
def post_productos(producto: Productos):
    return registrarNuevoProducto(producto)

@app.post("/api/v1/pedidos")
def post_pedidos(pedido: PedidoARegistrar):
    return registrarNuevoPedido(pedido)

@app.get("/api/v1/clientes/{cliente_id}/pedidos")
def get_pedidos(cliente_id: str):
    pedidos = consultarPedidos(cliente_id)
    return {"pedidos": pedidos}

@app.get("/api/v1/clientes/{cliente_id}/pedidos/{pedido_id}/estado")
def get_pedidos_especifico(cliente_id: str, pedido_id: str):
    pedido = consultarPedidoEspecifico(cliente_id, pedido_id)
    return {"id": pedido.id, "pedidos": pedido.estado}

@app.post("/api/v1/orders/")
def crear_pedido(pedido: PedidoARegistrar):
    return registrarNuevoPedido(pedido)

@app.get("/api/v1/orders/{order_id}/status")
def obtener_estado_pedido(order_id: str, cliente_id: str):
    return consultar_estado_pedido(order_id, cliente_id)

@app.put("/api/v1/orders/{order_id}/status")
def modificar_estado_pedido(order_id: str, estado_pedido: EstadoPedido, cliente_id: str):
    return actualizar_estado_pedido(order_id, estado_pedido, cliente_id)

@app.get("/api/v1/orders/")
def obtener_historial_pedidos(cliente_id: str):
    return listar_pedidos(cliente_id)

@app.put("/api/v1/clientes/{cliente_id}/pedidos/{pedido_id}/estado")
def actualizar_estado(cliente_id: str, pedido_id: str, estado_pedido: EstadoPedido):
    estado = estado_pedido.estado
    pedido_actualizado = actualizarEstadoPedido(cliente_id, pedido_id, estado)
    
    return {
        "message": "Estado del pedido actualizado correctamente.",
        "pedido_actualizado": {
            "id": pedido_actualizado.id,
            "estado": pedido_actualizado.estado
        }
    }
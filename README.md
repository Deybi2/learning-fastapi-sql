# learning-fastapi-sql

Este proyecto es una API para gestionar clientes, productos y pedidos.

## Endpoints

- `GET /api/saludo`: Saludo básico.
- `POST /api/v1/clientes`: Registrar un nuevo cliente.
- `POST /api/v1/productos`: Registrar un nuevo producto.
- `POST /orders/`: Crear un nuevo pedido.
- `GET /orders/{order_id}/status`: Consultar el estado de un pedido específico.
- `PUT /orders/{order_id}/status`: Actualizar el estado de un pedido.
- `GET /orders/`: Consultar el historial de pedidos de un cliente.
# Excepción personalizada exigida por la rúbrica
class StockInsuficienteError(Exception):
    pass

class InventarioService:
    def __init__(self):
        # Lista en memoria para almacenar los productos creados en la interfaz
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def obtener_productos(self):
        return self._productos

    def vender_producto(self, nombre_producto: str, cantidad: int):
        # Buscamos el producto por su nombre
        producto = next((p for p in self._productos if p.nombre == nombre_producto), None)
        if not producto:
            raise ValueError("El producto no existe en el inventario.")

        if cantidad > producto.stock:
            raise StockInsuficienteError(f"No hay suficiente stock. Disponible: {producto.stock}")
        
        # Descontamos el stock utilizando el setter del modelo
        producto.stock -= cantidad
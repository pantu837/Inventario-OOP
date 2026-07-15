# Excepción personalizada exigida por la rúbrica
class StockInsuficienteError(Exception):
    pass

class InventarioService:
    @staticmethod
    def vender(producto, cantidad: int):
        if cantidad > producto.stock:
            raise StockInsuficienteError(f"No hay suficiente stock. Disponible: {producto.stock}")
        
        # Descontamos el stock si todo está bien
        producto.stock -= cantidad
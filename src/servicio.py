from src.excepciones import StockInsuficienteError


class InventarioService:


    def __init__(self, dao):
        self.dao = dao


    def vender(self, id, cantidad):

        producto = self.dao.buscar_por_id(id)


        if producto is None:
            raise Exception("Producto no encontrado")


        if producto.stock < cantidad:
            raise StockInsuficienteError(
                "No hay suficiente stock"
            )


        producto.stock -= cantidad

        self.dao.actualizar(producto)

        return producto
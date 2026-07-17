class Producto:

    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

        self.validar_precio()
        self.validar_stock()


    def validar_precio(self):
        if self.precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")


    def validar_stock(self):
        if self.stock < 0:
            raise ValueError("El stock no puede ser negativo")

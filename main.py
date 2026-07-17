from src.db import crear_tabla
from src.modelo import Producto
from src.dao import ProductoDAO
from src.servicio import InventarioService
from src.excepciones import StockInsuficienteError


def menu():

    crear_tabla()

    dao = ProductoDAO()
    servicio = InventarioService(dao)


    while True:

        print("\n--- INVENTARIO ---")
        print("1. Registrar producto")
        print("2. Mostrar producto")
        print("3. Vender producto")
        print("4. Salir")


        opcion = input("Selecciona una opción: ")


        if opcion == "1":

            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))


            producto = Producto(
                None,
                nombre,
                precio,
                stock
            )


            dao.guardar(producto)

            print("Producto guardado correctamente")


        elif opcion == "2":

            id = int(input("ID del producto: "))

            producto = dao.buscar_por_id(id)


            if producto:

                print("\nProducto:")
                print("Nombre:", producto.nombre)
                print("Precio:", producto.precio)
                print("Stock:", producto.stock)

            else:

                print("Producto no encontrado")


        elif opcion == "3":

            id = int(input("ID producto: "))
            cantidad = int(input("Cantidad a vender: "))


            try:

                servicio.vender(id,cantidad)

                print("Venta realizada")


            except StockInsuficienteError as e:

                print(e)


        elif opcion == "4":

            break



if __name__ == "__main__":
    menu()

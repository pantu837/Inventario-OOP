from src.db import crear_tabla
from src.modelo import Producto
from src.dao import ProductoDAO


def main():

    crear_tabla()

    dao = ProductoDAO()


    producto = Producto(
        None,
        "Mouse",
        250,
        5
    )


    dao.guardar(producto)


    resultado = dao.buscar_por_id(1)


    print(resultado.nombre)
    print(resultado.precio)
    print(resultado.stock)



if __name__ == "__main__":
    main()
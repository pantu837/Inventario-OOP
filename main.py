from src.db import crear_tabla
from src.modelo import Producto


def main():

    crear_tabla()

    producto = Producto(
        1,
        "Mouse",
        -50,
        5
    )

    print(producto.nombre)
    print(producto.precio)
    print(producto.stock)


if __name__ == "__main__":
    main()
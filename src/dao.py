from src.db import get_connection
from src.modelo import Producto


class ProductoDAO:


    def guardar(self, producto):

        conexion = get_connection()

        cursor = conexion.cursor()

        cursor.execute(
            """
            INSERT INTO productos(nombre, precio, stock)
            VALUES (?, ?, ?)
            """,
            (
                producto.nombre,
                producto.precio,
                producto.stock
            )
        )

        conexion.commit()
        conexion.close()



    def buscar_por_id(self, id):

        conexion = get_connection()

        cursor = conexion.cursor()

        cursor.execute(
            """
            SELECT id, nombre, precio, stock
            FROM productos
            WHERE id = ?
            """,
            (id,)
        )

        fila = cursor.fetchone()

        conexion.close()


        if fila:

            return Producto(
                fila[0],
                fila[1],
                fila[2],
                fila[3]
            )

        return None



    def actualizar(self, producto):

        conexion = get_connection()

        cursor = conexion.cursor()

        cursor.execute(
            """
            UPDATE productos
            SET nombre=?, precio=?, stock=?
            WHERE id=?
            """,
            (
                producto.nombre,
                producto.precio,
                producto.stock,
                producto.id
            )
        )


        conexion.commit()
        conexion.close()
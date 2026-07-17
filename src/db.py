import sqlite3


def get_connection():
    return sqlite3.connect("inventario.db")


def crear_tabla():

    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL
    )
    """)

    conexion.commit()
    conexion.close()

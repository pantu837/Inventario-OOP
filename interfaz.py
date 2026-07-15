import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from src.db import crear_tabla
from src.modelo import Producto
from src.dao import ProductoDAO


crear_tabla()

dao = ProductoDAO()


def guardar():

    try:

        producto = Producto(
            None,
            entrada_nombre.get(),
            float(entrada_precio.get()),
            int(entrada_stock.get())
        )

        dao.guardar(producto)

        messagebox.showinfo(
            "Correcto",
            "Producto guardado"
        )

        limpiar()
        mostrar_productos()


    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


def mostrar_productos():

    for fila in tabla.get_children():
        tabla.delete(fila)


    conexion = dao.get_connection() if hasattr(dao,"get_connection") else None


    import sqlite3

    conexion = sqlite3.connect("inventario.db")

    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM productos"
    )

    productos = cursor.fetchall()


    for producto in productos:

        tabla.insert(
            "",
            tk.END,
            values=producto
        )


    conexion.close()



def limpiar():

    entrada_nombre.delete(0,tk.END)
    entrada_precio.delete(0,tk.END)
    entrada_stock.delete(0,tk.END)



ventana = tk.Tk()

ventana.title("Sistema Inventario OOP")
ventana.geometry("600x500")


titulo = tk.Label(
    ventana,
    text="Inventario OOP",
    font=("Arial",18)
)

titulo.pack()



tk.Label(
    ventana,
    text="Nombre"
).pack()

entrada_nombre=tk.Entry(ventana)
entrada_nombre.pack()



tk.Label(
    ventana,
    text="Precio"
).pack()

entrada_precio=tk.Entry(ventana)
entrada_precio.pack()



tk.Label(
    ventana,
    text="Stock"
).pack()

entrada_stock=tk.Entry(ventana)
entrada_stock.pack()



tk.Button(
    ventana,
    text="Guardar Producto",
    command=guardar
).pack(pady=10)



tabla = ttk.Treeview(
    ventana,
    columns=("ID","Nombre","Precio","Stock"),
    show="headings"
)


tabla.heading("ID",text="ID")
tabla.heading("Nombre",text="Nombre")
tabla.heading("Precio",text="Precio")
tabla.heading("Stock",text="Stock")


tabla.pack(
    expand=True,
    fill="both"
)


mostrar_productos()


ventana.mainloop()
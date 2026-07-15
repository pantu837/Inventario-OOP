import tkinter as tk
from tkinter import messagebox, ttk
# Importamos tus clases del modelo y el servicio
# Importamos la clase Producto de modelo
from src.modelo import Producto
# Importamos el servicio y la excepción desde servicio
from src.servicio import InventarioService, StockInsuficienteError

class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Inventario - UPVT")
        self.root.geometry("650x450")
        self.root.resizable(False, False)
        
        # Inicializamos el servicio de inventario
        self.servicio = InventarioService()
        
        # Estilos visuales sencillos
        self.root.configure(bg="#f3f4f6")
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        self.crear_componentes()
        self.actualizar_tabla()

    def crear_componentes(self):
        # --- TÍTULO ---
        titulo = tk.Label(
            self.root, 
            text="Gestión de Inventario (OOP + QA)", 
            font=("Helvetica", 16, "bold"), 
            bg="#f3f4f6", 
            fg="#1f2937"
        )
        titulo.pack(pady=10)

        # --- CONTENEDOR PRINCIPAL ---
        main_frame = tk.Frame(self.root, bg="#f3f4f6")
        main_frame.pack(fill="both", expand=True, padx=20, pady=5)

        # --- FORMULARIO (IZQUIERDA) ---
        form_frame = tk.LabelFrame(main_frame, text=" Registrar Producto ", font=("Helvetica", 10, "bold"), bg="#f3f4f6", fg="#4b5563")
        form_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

        tk.Label(form_frame, text="Nombre:", bg="#f3f4f6").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.txt_nombre = tk.Entry(form_frame, width=20)
        self.txt_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Precio ($):", bg="#f3f4f6").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.txt_precio = tk.Entry(form_frame, width=20)
        self.txt_precio.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Stock inicial:", bg="#f3f4f6").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.txt_stock = tk.Entry(form_frame, width=20)
        self.txt_stock.grid(row=2, column=1, padx=5, pady=5)

        btn_agregar = tk.Button(
            form_frame, 
            text="Agregar Producto", 
            command=self.agregar_producto, 
            bg="#10b981", 
            fg="white", 
            font=("Helvetica", 9, "bold"),
            relief="flat",
            activebackground="#059669"
        )
        btn_agregar.grid(row=3, column=0, columnspan=2, pady=15, ipadx=10)

        # --- TABLA DE PRODUCTOS (DERECHA) ---
        table_frame = tk.Frame(main_frame, bg="#f3f4f6")
        table_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.tabla = ttk.Treeview(table_frame, columns=("Nombre", "Precio", "Stock"), show="headings", height=10)
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Precio", text="Precio")
        self.tabla.heading("Stock", text="Stock")
        
        self.tabla.column("Nombre", width=120, anchor="center")
        self.tabla.column("Precio", width=80, anchor="center")
        self.tabla.column("Stock", width=80, anchor="center")
        self.tabla.pack(side="left", fill="both", expand=True)

        # --- SECCIÓN DE VENTA / RETIRO (ABAJO) ---
        action_frame = tk.LabelFrame(self.root, text=" Operaciones de Venta ", font=("Helvetica", 10, "bold"), bg="#f3f4f6", fg="#4b5563")
        action_frame.pack(fill="x", padx=30, pady=15)

        tk.Label(action_frame, text="Cantidad a vender:", bg="#f3f4f6").pack(side="left", padx=10, pady=10)
        self.txt_vender_cantidad = tk.Entry(action_frame, width=10)
        self.txt_vender_cantidad.pack(side="left", padx=10)

        btn_vender = tk.Button(
            action_frame, 
            text="Registrar Venta", 
            command=self.vender_producto, 
            bg="#ef4444", 
            fg="white", 
            font=("Helvetica", 9, "bold"),
            relief="flat",
            activebackground="#dc2626"
        )
        btn_vender.pack(side="left", padx=10, ipadx=10)

    # --- LÓGICA DEL NEGOCIO EN LA GUI ---

    def actualizar_tabla(self):
        # Limpiamos la tabla primero
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        # Cargamos los productos desde nuestro servicio
        for producto in self.servicio.obtener_productos():
            self.tabla.insert("", "end", values=(producto.nombre, f"${producto.precio:.2f}", producto.stock))

    def agregar_producto(self):
        try:
            nombre = self.txt_nombre.get().strip()
            precio = float(self.txt_precio.get())
            stock = int(self.txt_stock.get())

            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")

            # Intentamos instanciar el producto (aquí saltará el ValueError si el precio es negativo)
            nuevo_producto = Producto(nombre, precio, stock)
            self.servicio.agregar_producto(nuevo_producto)
            
            # Limpiamos los campos
            self.txt_nombre.delete(0, tk.END)
            self.txt_precio.delete(0, tk.END)
            self.txt_stock.delete(0, tk.END)

            self.actualizar_tabla()
            messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado correctamente.")

        except ValueError as ex:
            # Aquí capturamos precios negativos o campos vacíos/mal formateados
            messagebox.showerror("Error de Validación", f"Entrada inválida: {ex}")
        except Exception as ex:
            messagebox.showerror("Error", f"Ocurrió un error: {ex}")

    def vender_producto(self):
        selected_item = self.tabla.selection()
        if not selected_item:
            messagebox.showwarning("Atención", "Por favor, selecciona un producto de la lista.")
            return

        try:
            cantidad = int(self.txt_vender_cantidad.get())
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a 0.")

            # Obtenemos el nombre del producto seleccionado en la tabla
            valores = self.tabla.item(selected_item)['values']
            nombre_producto = valores[0]

            # Ejecutamos la transacción a través de nuestro servicio
            self.servicio.vender_producto(nombre_producto, cantidad)
            
            # Limpiamos la casilla de cantidad y refrescamos
            self.txt_vender_cantidad.delete(0, tk.END)
            self.actualizar_tabla()
            messagebox.showinfo("Venta Exitosa", f"Se retiraron {cantidad} unidades de '{nombre_producto}'.")

        except ValueError as ex:
            messagebox.showerror("Error de Formato", str(ex))
        except StockInsuficienteError as ex:
            # ¡Aquí capturamos tu excepción personalizada!
            messagebox.showerror("Sin Stock Suficiente", str(ex))
        except Exception as ex:
            messagebox.showerror("Error", str(ex))


# Código para arrancar la aplicación directamente
if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()
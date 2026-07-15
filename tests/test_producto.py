import unittest
# Importamos la clase Producto y el Servicio de inventario
from src.modelo import Producto
from src.servicio import InventarioService, StockInsuficienteError

class TestInventario(unittest.TestCase):

    def test_crear_producto_valido(self):
        """1. CASO FELIZ: Crear un producto con datos correctos"""
        prod = Producto(nombre="Mouse", precio=150.0, stock=10)
        self.assertEqual(prod.nombre, "Mouse")
        self.assertEqual(prod.precio, 150.0)
        self.assertEqual(prod.stock, 10)

    def test_precio_negativo_lanza_value_error(self):
        """2. CASO DE ERROR (ValueError): Validar que precio negativo truene"""
        with self.assertRaises(ValueError) as context:
            # Esto debe lanzar ValueError según los requerimientos del profesor
            Producto(nombre="Mouse", precio=-50.0, stock=5)
        
        self.assertIn("El precio debe ser mayor a 0", str(context.exception))

    def test_vender_mas_stock_lanza_excepcion(self):
        """3. CASO DE EXCEPCIÓN CUSTOM: Vender más de lo disponible"""
        prod = Producto(nombre="Teclado", precio=500.0, stock=3)
        
        # Debe lanzar la excepción personalizada que hizo tu compañero de Lógica
        with self.assertRaises(StockInsuficienteError):
            InventarioService.vender(prod, cantidad=10)

if __name__ == "__main__":
    unittest.main()
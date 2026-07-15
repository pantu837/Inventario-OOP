# Inventario OOP

Sistema de inventario desarrollado en Python aplicando Programación Orientada a Objetos.

## Arquitectura

Producto
↓
ProductoDAO
↓
SQLite

InventarioService controla las reglas del negocio.

## Ramas del proyecto

main
- Rama principal protegida.

feature/lider
- Arquitectura, integración y documentación.

feature/backend
- Modelo y acceso a datos.

feature/servicio
- Lógica del inventario y excepciones.

feature/tests
- Pruebas unitarias.

## Instalación

Crear entorno virtual:

python -m venv venv

Activar:

venv\Scripts\activate

Instalar dependencias:

pip install -r requirements.txt
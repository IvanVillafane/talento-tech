Inventario de Productos - Aplicación de Consola con SQLite

###Requisitos Previos##
Python 3 debe estar instalado en tu sistema.
SQLite ya viene incluido con Python, por lo que no es necesario instalarlo.

1-Instalación
Clona o descarga este repositorio en tu computadora.
Asegúrate de tener Python instalado ejecutando el siguiente comando en tu terminal:

python --version
pip install

Ejecución de la Aplicación

python python.py

Funcionalidades
--- Menú de Inventario ---
1. Agregar producto
2. Mostrar productos
3. Actualizar producto
4. Eliminar producto
5. Buscar producto
6. Generar reporte
7. Salir


Descripción de las Opciones del Menú

Agregar producto: Permite agregar un nuevo producto al inventario. Se solicita el nombre, descripción, cantidad, precio y categoría del producto.

Mostrar productos: Muestra todos los productos almacenados en el inventario. Cada producto incluye los siguientes datos:

ID
Nombre
Descripción
Cantidad
Precio
Categoría

Actualizar producto: Permite actualizar los datos de un producto existente en la base de datos. Se debe proporcionar el ID del producto que deseas modificar y los nuevos valores para cada campo.

Eliminar producto: Elimina un producto del inventario. Se solicita el ID del producto que se desea eliminar.

Buscar producto: Permite buscar productos en el inventario por nombre. La búsqueda devuelve todos los productos cuyo nombre contiene el término ingresado.

Generar reporte: Muestra un resumen de la cantidad total de productos agrupados por categoría. Esta opción es útil para ver rápidamente cuántos productos hay en cada categoría.

Salir: Cierra la aplicación.


##Notas
La base de datos se almacena en el archivo inventario.db. Si este archivo no existe, se creará automáticamente la primera vez que ejecutes la aplicación.
Los datos se guardan de forma persistente en inventario.db, por lo que puedes cerrar la aplicación y volver a ejecutarla sin perder los productos que has registrado.
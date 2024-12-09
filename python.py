import sqlite3
from colorama import Fore, Back, Style, init

# Inicializar colorama
init(autoreset=True)


# Crear la conexión y la tabla si no existen
def crear_tabla():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
    """
    )
    conexion.commit()
    conexion.close()
    print(Fore.GREEN + "Tabla 'productos' creada o ya existente.")


# Agregar un producto
def agregar_producto(nombre, descripcion, cantidad, precio, categoria):
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute(
        """
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    """,
        (nombre, descripcion, cantidad, precio, categoria),
    )
    conexion.commit()
    conexion.close()
    print(Fore.CYAN + f"Producto '{nombre}' agregado con éxito.")


# Mostrar productos
def mostrar_productos():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()
    if not productos:
        print(Fore.YELLOW + "No hay productos registrados.")
    else:
        print(Fore.MAGENTA + "\n--- Productos en el Inventario ---")
        for producto in productos:
            print(
                f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, "
                f"Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}"
            )


# Actualizar un producto
def actualizar_producto(id, nombre, descripcion, cantidad, precio, categoria):
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute(
        """
        UPDATE productos SET nombre=?, descripcion=?, cantidad=?, precio=?, categoria=? 
        WHERE id=?
    """,
        (nombre, descripcion, cantidad, precio, categoria, id),
    )
    conexion.commit()
    conexion.close()
    print(Fore.BLUE + f"Producto ID {id} actualizado con éxito.")


# Eliminar un producto
def eliminar_producto(id):
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id=?", (id,))
    conexion.commit()
    conexion.close()
    print(Fore.RED + f"Producto ID {id} eliminado con éxito.")


# Buscar productos
def buscar_producto(nombre):
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", ("%" + nombre + "%",))
    productos = cursor.fetchall()
    conexion.close()
    if productos:
        print(Fore.CYAN + "\n--- Resultados de la Búsqueda ---")
        for producto in productos:
            print(
                f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, "
                f"Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}"
            )
    else:
        print(Fore.YELLOW + f"No se encontraron productos con el nombre '{nombre}'.")


# Generar un reporte
def generar_reporte():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT categoria, SUM(cantidad) FROM productos GROUP BY categoria")
    reporte = cursor.fetchall()
    conexion.close()
    print(Fore.GREEN + "\n--- Reporte de Inventario por Categoría ---")
    for categoria, total in reporte:
        print(f"Categoría: {categoria}, Total de productos: {total}")


# Menú principal
def mostrar_menu():
    print(Fore.MAGENTA + "\n--- Menú de Inventario ---")
    print(Fore.GREEN + "1. Agregar producto")
    print(Fore.GREEN + "2. Mostrar productos")
    print(Fore.GREEN + "3. Actualizar producto")
    print(Fore.GREEN + "4. Eliminar producto")
    print(Fore.GREEN + "5. Buscar producto")
    print(Fore.GREEN + "6. Generar reporte")
    print(Fore.RED + "7. Salir")


# Función principal
def main():
    crear_tabla()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            descripcion = input("Descripción del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            categoria = input("Categoría del producto: ")
            agregar_producto(nombre, descripcion, cantidad, precio, categoria)

        elif opcion == "2":
            mostrar_productos()

        elif opcion == "3":
            id = int(input("ID del producto a actualizar: "))
            nombre = input("Nuevo nombre del producto: ")
            descripcion = input("Nueva descripción del producto: ")
            cantidad = int(input("Nueva cantidad del producto: "))
            precio = float(input("Nuevo precio del producto: "))
            categoria = input("Nueva categoría del producto: ")
            actualizar_producto(id, nombre, descripcion, cantidad, precio, categoria)

        elif opcion == "4":
            id = int(input("ID del producto a eliminar: "))
            eliminar_producto(id)

        elif opcion == "5":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            buscar_producto(nombre)

        elif opcion == "6":
            generar_reporte()

        elif opcion == "7":
            print(Fore.RED + "Saliendo de la aplicación...")
            break

        else:
            print(Fore.YELLOW + "Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()

# Clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    # Método para mostrar detalles del producto
    def mostrar_detalles(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}")


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    # Método para agregar un producto al inventario
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Método para eliminar un producto del inventario por su nombre
    def eliminar_producto(self, producto_nombre):
        self.productos = [p for p in self.productos if p.nombre != producto_nombre]

    # Método para mostrar todos los productos en el inventario
    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos:
                producto.mostrar_detalles()
        else:
            print("El inventario está vacío.")


# Función para agregar productos de forma interactiva
def agregar_producto_interactivo(inventario):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))

    # Crear una instancia del producto con los datos ingresados
    producto = Producto(nombre, precio, cantidad)

    # Agregar el producto al inventario
    inventario.agregar_producto(producto)
    print("Producto agregado exitosamente.")


# Crear instancia del inventario
inventario = Inventario()

# Ciclo para agregar varios productos
while True:
    print("\nOpciones: ")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Eliminar producto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto_interactivo(inventario)
    elif opcion == "2":
        inventario.mostrar_inventario()
    elif opcion == "3":
        nombre_producto = input("Ingrese el nombre del producto a eliminar: ")
        inventario.eliminar_producto(nombre_producto)
        print("Producto eliminado.")
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")

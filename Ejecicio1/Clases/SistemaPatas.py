from Clases.Mascota import Mascota
from Clases.Cliente import Cliente
from Clases.Producto import Producto
from Clases.Venta import Venta

class SistemaPatasFelices:
    def __init__(self):
        self.mascotas = []
        self.clientes = []
        self.productos = []
        self.ventas = []
    def agregar_mascota(self, mascota):
        nombre= input("Ingrese el nombre de la mascota: ")
        edad = input("Ingrese la edad de la mascota: ")
        dueno = input("Ingrese el nombre del dueño de la mascota: ")
        mascota=Mascota(nombre,edad,dueno)
        self.mascotas.append(mascota)
        print(f"Se ha agregado la mascota: {mascota.nombre}")
    def mostrar_mascotas(self):
        if not self.mascotas:
            print("No hay mascotas registradas.")
        else:
            print("Lista de mascotas:")
            for mascota in self.mascotas:
                print(mascota.mostrar_informacion())
    def agregar_cliente(self, cliente):
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        edad = input("Ingrese la edad del cliente: ")
        cliente = Cliente(nombre, apellido, edad)
        self.clientes.append(cliente)
        print(f"Se ha agregado el cliente: {cliente.nombre} {cliente.apellido}")
    def mostrar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            print("Lista de clientes:")
            for cliente in self.clientes:
                print(cliente)
    def agregar_producto(self, producto):
        nombre = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")
        cantidad =  int(input("Ingrese la cantidad del producto: "))
        producto = Producto(nombre, precio, cantidad)
        self.productos.append(producto)
        print(f"Se ha agregado el producto: {producto.nombre}")
    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos registrados.")
        else:
            print("Lista de productos:")
            for producto in self.productos:
                print(producto.mostrar_informacion())
    def realizar_venta(self, venta):
        id_cliente = input("Ingrese el nombre del cliente: ")
        id_producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad vendida: "))
        cliente = next((c for c in self.clientes if c.nombre.lower() == id_cliente.lower()), None)
        producto = next((p for p in self.productos if p.nombre.lower() == id_producto.lower()), None)
        if not cliente:
            print("Cliente no encontrado.")
            return
        if not producto:
            print("Producto no encontrado.")
            return
        if producto.cantidad>=cantidad:
            precioo_unitario = producto.precio*cantidad
            producto.cantidad -= cantidad
            venta = Venta(cliente.nombre, producto.nombre, cantidad,precioo_unitario)
            self.ventas.append(venta)
            print(f"Venta realizada:  Cliente: {venta.id_cliente}, Producto: {venta.id_producto}, Cantidad: {venta.cantidad}, Precio total: {precioo_unitario}")
        else:
            print("No hay suficiente cantidad del producto para realizar la venta.")
    def mostrar_ventas(self):
        if not self.ventas:
            print("No hay ventas registradas.")
        else:
            print("Lista de ventas:")
            for venta in self.ventas:
                print(venta.mostrar_detalles())
   

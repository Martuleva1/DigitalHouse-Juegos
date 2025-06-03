class Venta:
    def __init__(self, id_cliente, id_producto, cantidad, precio_unitario):
        self.id_cliente = id_cliente
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def calcular_total(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"Venta(id_cliente={self.id_cliente}, id_producto={self.id_producto}, cantidad={self.cantidad}, precio_unitario={self.precio_unitario})"
    def aplicar_descuento(self, porcentaje):
        descuento = self.precio_unitario * (porcentaje / 100)
        self.precio_unitario -= descuento
        return self.precio_unitario
    def mostrar_detalles(self):
        return f"Detalles de la venta: {self.id_cliente}, {self.id_producto}, {self.cantidad}, {self.precio_unitario}"
    def mostrar_total(self):
        total = self.calcular_total()
        return f"El total de la venta es: {total}"
    def mostrar_descuento(self, porcentaje):
        nuevo_precio = self.aplicar_descuento(porcentaje)
        return f"El nuevo precio después de aplicar un descuento del {porcentaje}% es: {nuevo_precio}"
    def realizarventa(self):
        return f"Venta realizada: {self.id_cliente}, Producto: {self.id_producto}, Cantidad: {self.cantidad}, Precio total: {self.precio_total}"
    def transaccion(self):
        return f"Transacción de venta: {self.id_cliente}, Producto: {self.id_producto}, Cantidad: {self.cantidad}, Precio total: {self.precio_total}"
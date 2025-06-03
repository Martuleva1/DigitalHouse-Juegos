class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Producto(nombre={self.nombre}, precio={self.precio}, cantidad={self.cantidad})"

    def calcular_total(self):
        return self.precio * self.cantidad
    
    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        return self.precio
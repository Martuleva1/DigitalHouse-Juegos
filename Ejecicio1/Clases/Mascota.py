class Mascota:
    def __init__(self, nombre, edad, dueno):
        self.nombre = nombre
        self.dueno = dueno
        self.edad = edad
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Dueño: {self.dueno}, Edad: {self.edad} años"
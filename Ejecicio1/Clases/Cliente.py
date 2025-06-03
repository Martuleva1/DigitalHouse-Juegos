class Cliente:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Edad: {self.edad}"
    def mascota(self, mascota):
        return f"{self.nombre} tiene una mascota llamada {mascota.nombre}."
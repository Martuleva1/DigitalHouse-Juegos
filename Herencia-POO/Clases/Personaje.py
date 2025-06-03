class Personaje:
    def __init__(self,nombre,salud):
        self.nombre = nombre
        self.salud = salud
    def Identificarse(self):
        return f"Soy {self.nombre}"
    def mostrar_salud(self):
        return f"{self.nombre} tiene {self.salud} punto de salud."  
    


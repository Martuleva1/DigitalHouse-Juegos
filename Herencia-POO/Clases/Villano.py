from Clases.Personaje import Personaje
class Villano(Personaje):
    def __init__(self, nombre, salud, maldad):
        super().__init__(nombre, salud)
        self.maldad = maldad

    def MostrarMaldad(self):
        return f"{self.nombre} tiene un nivel de maldad de {self.maldad}."
    
    def Identificarse(self):
        return f"Soy {self.nombre}, el villano con un nivel de maldad de {self.maldad}."
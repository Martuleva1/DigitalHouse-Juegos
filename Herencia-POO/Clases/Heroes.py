from Clases.Personaje import Personaje
class Heroe(Personaje):
    def __init__(self,nombre,salud,poder):
        super().__init__(nombre,salud)
        self.poder=poder
    
    def MostrarPoder(self):
        return f"{self.nombre} tiene el poder de {self.poder}."
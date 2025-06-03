class Mago:
    def __init__ (self,nombre, hechizos=None):
        self.__nombre = nombre
        self.__hechizos = hechizos if hechizos is not None else []
    
    #metodo ToString
    def __str__ (self):
        return f"Mago: {self.__nombre}"
    def __len__(self):
        return len(self.__hechizos)
    def __eq__(self, otro_mago):
        return self.__nombre == otro_mago.__nombre and self.__hechizos == otro_mago.__hechizos


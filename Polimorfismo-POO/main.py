from Clases.Gato import Gato
from Clases.Perro import Perro
def HacerSonido(animal):
    print(f"{animal.nombre} hace {animal.hacer_sonido()}")

perro= Perro("Firulais")
gato = Gato("Misa")
HacerSonido(perro)  # Imprime: Guau
HacerSonido(gato)   # Imprime: Miau

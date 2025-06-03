from Clases.Heroes import Heroe
from Clases.Villano import Villano

superman = Heroe("Superman", 100, "Vuelo")
joker = Villano("Joker", 80, "Caos")
print(superman.Identificarse())#Metodo heredado de Personaje
print(joker.Identificarse()) #metodo heredado de Personaje
print(superman.mostrar_salud()) #Metodo heredado de Personaje
print(joker.mostrar_salud()) #Metodo heredado de Personaje
print(superman.MostrarPoder())#Metodo propio de Heroe
print(joker.MostrarMaldad())#Metodo propio de Villano
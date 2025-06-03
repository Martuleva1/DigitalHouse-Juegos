#Funciones con argumentos
from functools import reduce


def aplicarfuncion(a, b):
    """Suma dos números."""
    return a(b)

def Cuadrado(x):
    """Calcula el cuadrado de un número."""
    return x * x
def cubo(x):
    """Calcula el cubo de un número."""
    return x * x * x
print(aplicarfuncion(Cuadrado, 5))
print(aplicarfuncion(cubo, 5))

#MAP
def Cuadrado(x):
    """Calcula el cuadrado de un número."""
    return x * x
numero =[1,2,3,4,5,6,7,8,9,10]
Cuadrados= list(map(Cuadrado, numero))
print("Lista de números:", numero)
print("Lista de cuadrados:", Cuadrados)

#filter
def es_par(x):
    """Verifica si un número es par."""
    return x % 2 == 0

pares= list(filter(es_par, numero))
print("Lista de números:", numero)  
print("Lista de números pares:", pares)
#reduce
def suma(x, y):
    """Suma dos números."""
    return x + y
sumatoria = reduce(suma, numero)
print("Lista de números:", numero)  
print("Suma de todos los números:", sumatoria)

#closure
def exterior(x):
    def interior(y):
        return x + y
    return interior
closure_func = exterior(5)
print("Resultado de la función closure:", closure_func(10))  # Imprime 15

#DECORADORES
def decorador(funcion):
    def envoltorio():
        print("Antes de llamar a la función decorada")
        funcion()
        print("Después de llamar a la función decorada")
    return envoltorio

def saludar():
    print("¡Hola desde la función decorada!")
saludar_decorada = decorador(saludar)
saludar_decorada()  # Llama a la función decorada
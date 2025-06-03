from unittest import result


def Saludar(nombre):
    print("Hola, ¿cómo estás?",nombre)
def Padre(hijo1,hijo2,hijo3):
    print("Hijos:", hijo1, hijo2, hijo3)
    print("el mas pequeño es:", hijo3)
# Ejemplo de uso de las funciones lista
def listas_hijos(hijos):
    print("Lista de hijos:")
    for hijo in hijos:
        print("-", hijo)
def sumar(a,b):
    return a + b

Saludar("Martina")
Padre(hijo1="Juan",hijo2="Pedro", hijo3="Luis")
hijos = ["Juan", "Pedro", "Luis"]
listas_hijos(hijos)
#suma
resultado = sumar(5, 10)
print("La suma es:", resultado)

#recursiva
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Ejemplo de uso de la función recursiva
numero = 5
resultado_factorial = factorial(numero)
print(f"El factorial de {numero} es: {resultado_factorial}")

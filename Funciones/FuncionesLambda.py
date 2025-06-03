#lambda
def duplicar(x):
    return x * 2

print(duplicar(5))

duplicar_lambda = lambda num:num*2
print(duplicar_lambda(5))

#MULTIPLICAR
def multiplicar(x, y):
    return x * y

print(multiplicar(5, 10))

multiplicar_lambda = lambda a, b: a * b
print(multiplicar_lambda(5, 10))

#funciones lambda multiplicador
def multiplicador(factor):
    return lambda x: x * factor
multiplicar_por_3 = multiplicador(3)
print(multiplicar_por_3(5))  # Imprime 15

#diccionario con funciones lambda
operaciones = {
    'suma': lambda x, y: x + y,
    'resta': lambda x, y: x - y,
    'multiplicacion': lambda x, y: x * y,
    'division': lambda x, y: x / y if y != 0 else 'Error: División por cero'
}
#ordenar diccionario con lambda
def ordenar_diccionario(diccionario):
    return dict(sorted(diccionario.items(), key=lambda item: item[0]))
# Ejemplo de uso del diccionario de operaciones
resultado_suma = operaciones['suma'](5, 10)
print(f"Resultado de la suma: {resultado_suma}")
resultado_resta = operaciones['resta'](10, 5)
print(f"Resultado de la resta: {resultado_resta}")
resultado_multiplicacion = operaciones['multiplicacion'](5, 10)
print(f"Resultado de la multiplicación: {resultado_multiplicacion}")
resultado_division = operaciones['division'](10, 2)
print(f"Resultado de la división: {resultado_division}")
resultado_division_error = operaciones['division'](10, 0)
print(f"Resultado de la división con error: {resultado_division_error}")

# Ordenar el diccionario de operaciones
operaciones_ordenadas = ordenar_diccionario(operaciones)
print("\nDiccionario de operaciones ordenado:")
print(operaciones_ordenadas)
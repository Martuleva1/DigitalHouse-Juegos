#Diccionarios no ordenada de pares clave-valor
diccionario={
    "Nombre": "Martina",
    "Edad": "23",
    "Tecnologias": ["Python","js"]
}
print("Diccionario original:")
print(diccionario)
#Obtener nombre
nombre= diccionario.get("Nombre")
print(nombre)
#Obtener claves
claves = diccionario.keys()
print(claves)
#agregar primo
diccionario["Primo"] = "Lucas"
print("\nDiccionario después de agregar 'Primo':")
print(claves)
print(diccionario)
#valores
valores = diccionario.values()
print("\nValores del diccionario:")
print(valores)
#for
print("\nRecorriendo el diccionario con For:")
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")
#Anidados
diccionario_anidado = {
    "Nombre": "Martina",
    "Edad": 23,
    "Tecnologias": ["Python", "js"],
    "Direccion": {
        "Calle": "Falsa",
        "Numero": 123
    }
}
print("\nDiccionario anidado:")
print(diccionario_anidado)
#Acceder a un valor anidado
direccion = diccionario_anidado["Direccion"]
print(direccion)
#for
for clave, valor in diccionario_anidado.items():
    if isinstance(valor, dict):  # Verifica si el valor es un diccionario
        print(f"{clave}:")
        for subclave, subvalor in valor.items():
            print(f"  {subclave}: {subvalor}")
    else:
        print(f"{clave}: {valor}")
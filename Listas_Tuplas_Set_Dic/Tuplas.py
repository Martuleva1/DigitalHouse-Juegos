#TUPLAS

frutas=("Mandarina","Banana","Pera","Manzana","Kiwi","Melon")
print("Tupla de frutas:")
print(frutas)
#tamaño
print("\nTamaño de la tupla:")
print(len(frutas))
#Tipo de tupla
print("\nTipo de la tupla:")
print(type(frutas))

#lo combierto a lista
frutas_lista = list(frutas)
print("\nTupla convertida a lista:")
print(frutas_lista)
#lo modifico
frutas_lista[0] = "Naranja"
print("\nLista de frutas modificada:")
print(frutas_lista)
#lo vuelvo a convertir a tupla
frutas_modificada = tuple(frutas_lista) 
print("\nTupla de frutas modificada:")
print(frutas_modificada)

#For
print("\nRecorriendo la tupla con For:")
for fruta in frutas:
    print(fruta)
#For con índice disponible
print("\nRecorriendo la tupla con For y índice:")
for i in range(len(frutas)):
    print(f"Fruta {i+1}: {frutas[i]}")
#While
print("\nRecorriendo la tupla con While:")
i = 0
while i < len(frutas):
    print(f"Fruta {i+1}: {frutas[i]}")
    i += 1
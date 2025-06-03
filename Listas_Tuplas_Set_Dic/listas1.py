#Listas

#lista=["Mandarina","Banana","Pera"]
#print(lista)

#if "Manzana" in lista:
   # print("La fruta Manzana está en la lista")
#else:
 #  lista.insert(0,"Manzana")  
#print(lista)

lista1=["Mandarina","Banana","Pera","Manzana","Kiwi","Melon"]
#print(lista1)
#lista1.clear()  
#print(lista1)

#For
print("Recorriendo la lista con For:")
for fruta in lista1:
    print(fruta)

#For con indie disponible
print("\nRecorriendo la lista con For y índice:")
for i in range(len(lista1)):
    print(f"Fruta {i+1}: {lista1[i]}")

#While
print("\nRecorriendo la lista con While:")
i=0
while i < len(lista1):
    print(f"Fruta {i+1}: {lista1[i]}")
    i += 1

#Ordenar Listas
numero = [2,22,1,4,5,11,77,33,6]
numero.sort(reverse=True)
lista1.sort()
print("\nLista ordenada alfabéticamente:")
print(lista1)
print("\nLista de números ordenada al reves:")
print(numero)

#Copiar y juntar listas
copia_fruta = lista1.copy()
print("\nLista copiada:")
print(copia_fruta)
lista2=["Mandarina","Banana","Anana","Limon","Naranja"]
frutas = lista1 + lista2
print("\nLista de frutas combinada:")
print(frutas)
#otra opcion
lista1.extend(lista2)
print("\nLista de frutas combinada con extend:")
print(lista1)
#Contar cuantas veces 
print("\nContando cuántas veces aparece 'Banana' en la lista:")
print(lista1.count("Banana"))
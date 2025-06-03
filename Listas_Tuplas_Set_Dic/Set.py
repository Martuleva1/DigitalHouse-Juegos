#Set Conjuntos

conjunto_frutas = {"Mandarina","Banana","Pera","Manzana","Kiwi","Melon"}
lista_tropicales = ["Piña","Papaya","Mango"]
print("Conjunto de frutas:")
print(conjunto_frutas)
conjunto_frutas.update(lista_tropicales)  # Agregar varios elementos desde una lista
conjunto_frutas.add("Naranja")  # Agregar un elemento
#Borrar Banana
conjunto_frutas.discard("Banana")  # Elimina "Banana" si existe, no genera error si no está
#for
for conjunto_fruta in conjunto_frutas:
    print(conjunto_fruta)


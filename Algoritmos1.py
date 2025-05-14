#el usuario quiere saber cuantas letras tiene una palabra

#el usuario ingresa la palabra
palabra = input("Ingrese una palabra: ")
#el usuario ingresa la letra que quiere contar
letra = input("Ingrese la letra que desea contar: ")
#inicializamos el contador
contador = 0    
#recorremos la palabra
for i in range(len(palabra)):
    if palabra[i] == letra:
        contador += 1
#imprimimos el resultado        
print("La letra", letra, "se repite", contador, "veces en la palabra", palabra)
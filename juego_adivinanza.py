import random

from sqlalchemy import false, true



numero_secreto=random.randint(1,101)
adivinado = False
cant_intentos= 0
cant_max=5

print("BIENVENIDO A ADIVINAR EL NUMERO")
while not adivinado and cant_intentos<cant_max:
    entrada=int(input("Introduce un numero del 1 al 100: ")) #TODO: convertir a numero
    numero=int(entrada)
    if numero == numero_secreto:
        print("El numero es el correcto.")
        adivinado=true
    elif numero < numero_secreto:
        print("El numero es mayor al ingresado")
        continue
    else:
         print("El numero es menor al ingresado")
         continue
    cant_intentos+=1
if not cant_intentos<cant_max:
    print("Game over")
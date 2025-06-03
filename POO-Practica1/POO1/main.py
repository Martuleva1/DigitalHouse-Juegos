from Clases import Perro
    
perro1= Perro("Firulais", 3) #pasar el nombre y la edad
perro2 = Perro("Mirian",6)
print(f"El perro {perro1.nombre} de {perro1.edad} años dice: {perro1.Ladrar()}")
print(f"El perro {perro2.nombre} de {perro2.edad} años dice: {perro2.Ladrar()}")
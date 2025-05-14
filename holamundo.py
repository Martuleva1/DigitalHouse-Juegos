#sintaxis de codigo
#Indentacion
# Es el espacio en blanco llamada tabulacion o sangria al comienxo de una linea de codigo.
# el alcance no delimitara por llaves sino a traves de a indentacion ejempli
#-------------------------



from tkinter import Variable


for i in range(5):
        print (i)

#----------------
print(i)

# Variables
#Contenedores q almacenan datos que pueden cambiar durante la ejecucion

x=5
nombre= "Juan"
y = str(5)#casteo (cambiar el tipo de formato)
print(x)
print(nombre)
print(y)

#Tipod de Datos
#Texto
# str (cadena de caracteres)
texto = "Cadena de caracteres"

#Numericos
#int , Float y complejo

#Secuencia
#list(list) ordenada y mutable
lista= [1,2,3,4]
print(lista)
#tuple ordenada y inmutable
tupla = (1,2,3,4)
print(tupla)
#range secuencia inmutable de numeros
rango=range(0,10)
print(rango)
#Mapping Type mapeo

#dict (diccionario) Siempre clave y despues el valor.

diccionario= {"nombre":"Martina","Edad":"23"}
print(diccionario)
#SET TYPES
#set (conjunto) coleccion no ordenada y mutable de elementos unicos.
conjunto ={1,2,3,4}
print(conjunto)
#frozenset conjunto inmutable
conjunto_inmutable = frozenset({1,2,3,4})
print(conjunto_inmutable)
#Boolean Types
#boolean

#Casteo
#1ero texto
variable1="Texto1"
variable2="12345"
variable3="Texto123"

#Numericas
variable4=10
variable5=2.4
variable6=1j

print(type(variable1))
print(type(variable2))
print(type(variable3))
print(type(variable4))
print(type(variable5))
print(type(variable6))

#Cadena de caracteres 1
#Indice es el lugar o posicion donde el elemento en una estructura
#0 es h
#1 es o
#2 es l
txt="Hola mundo"
print(txt[0])
#cuantos caracteres tiene
int = len(txt)
print(int)

#slicing ponemos desede un caracter hasta un caracter NO incluido
tx="Seguimos trabajando con Strings"
print(tx[:8])

# Mayus a minu = lower y minu a mayus = upper y Primera letra mayus = capitalize primeras letras en mayus = title 
t="CUANDO ESTOY ESCRIBIENDO EN MAYUSCULA"
minuscula=t.lower()
print(minuscula)

#Corregir espacios
x="               uy! Me deje algunos espacios         "
textocorregido=x.strip()
print(textocorregido)

#Contatenar cadenas
a="Hola"
b="Mundo"
c=a+" "+b
print(c)
#otra opcion
horas=10
bb="El contenenido de este curso va a durar: {0} horas "
print(bb.format(horas))


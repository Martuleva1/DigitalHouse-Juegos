#Operadores
#Son simbolos o conjuntos de simbolos que realizan una operacion especifica en uno o mas operandos

#Tipos
#Aritmeticos - Comparacion - Logicos - Asignacion - Pertenencia - Identidad

#Aritmeticos
# // para dividir entero
# % resto
# ** exponenciacion
#a=8
#b=4
#c=a//b
#d=a%b
#e= a**b
#print(c)
#print(e)

#Asignacion



x=10
sumatorio = 3
x+=sumatorio
x+=sumatorio
x+=sumatorio
restar=2
x-=restar
multiplicar=2
x*=multiplicar
dividir=2
x//=dividir
print(x)

#Comparacion
x=5
y=2
print(x==y)#Q si 
print(x!=y) #Q no
print(x>y)#Mayor y < menos

#Logicos
#and or o Not

#Identidad
#is o is not

#Pertenencia
#in o in not

#Estrucuturas de Control
#If, ilif, else
x=0
if x>0:
    print("x es un numero positivo")
elif x<0:
    print("x es negativo")
else:
    print("x es 0")

#while
contador=0
while contador<5:
    contador+=1
    print("el contador es: ",contador)

#For
for i in range(5):
    print(i)

#Try, except, finally
a=10
b=5
try:
    resultado=a/b
    print(resultado)
except ZeroDivisionError:
    print("No se puede dividir por 0")
finally:
    resultado = 0
    print(resultado)

#break
contador=0
while contador<10:
    print(contador)
    if(contador==5):
        break
    contador+=1
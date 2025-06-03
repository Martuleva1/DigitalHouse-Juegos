from Clases.Cuenta_bancaria import CuentaBancaria
cuenta = CuentaBancaria("Juan Perez", 1000)

#print(cuenta.__saldo)#accesso directo al atributo privado, no recomendado

cuenta.Obtener_Saldo()#acceso al atributo privado a traves del metodo getter
cuenta.Depositar(0)
print(cuenta.Obtener_Saldo())  # Imprime: 1500
cuenta.Retirar(1000)
print(cuenta.Obtener_Saldo())  # Imprime: 1300

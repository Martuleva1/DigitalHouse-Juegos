class CuentaBancaria:
    def __init__ (self, titular,saldo_inicial):
        self.__titular = titular
        self.__saldo = saldo_inicial#con dos espacios se indica que es privado

    def Depositar(self, cantidad):
        if cantidad >0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Error: La cantidad a depositar debe ser positiva.")
    def Retirar (self,cantidad):
        if 0 < cantidad <=self.__saldo:
             self.__saldo -=cantidad
             print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}, se ha retirado {cantidad}")
        else:
            print("Error: Cantidad inválida o saldo insuficiente.") 
    #Getters
    def Obtener_Saldo(self):
        return self.__saldo
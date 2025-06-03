from Clases.SistemaPatas import SistemaPatasFelices
from Clases.Mascota import Mascota
from Clases.Cliente import Cliente
from Clases.Producto import Producto
from Clases.Venta import Venta
def menu():
        sistema = SistemaPatasFelices()
        while True:
            print("\n--- Sistema Patas Felices ---")
            print("1. Agregar Mascota")
            print("2. Mostrar Mascotas")
            print("3. Agregar Cliente")
            print("4. Mostrar Clientes")
            print("5. Agregar Producto")
            print("6. Mostrar Productos")
            print("7. Realizar Venta")
            print("8. Mostrar Ventas")
            print("9. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                sistema.agregar_mascota(Mascota("", "", ""))
            elif opcion == "2":
                sistema.mostrar_mascotas()
            elif opcion == "3":
                sistema.agregar_cliente(Cliente("", "", ""))
            elif opcion == "4":
                sistema.mostrar_clientes()
            elif opcion == "5":
                sistema.agregar_producto(Producto("", 0, 0))
            elif opcion == "6":
                sistema.mostrar_productos()
            elif opcion == "7":
                sistema.realizar_venta(Venta("","", 0, 0))
            elif opcion == "8":
                sistema.mostrar_ventas()
            elif opcion == "9":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida, intente de nuevo.")


menu()
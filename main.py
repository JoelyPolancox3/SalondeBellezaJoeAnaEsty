from funciones import *

def menu():
    limpiar_pantalla()
    print("   SALON DE BELLEZA - GESTION DE CLIENTES")
    print("1. Mostrar todos los clientes")
    print("2. Registrar nuevo cliente")
    print("3. Buscar cliente por ID")
    print("4. Actualizar precio de servicio")
    print("5. Eliminar cliente")
    print("7. Salir")
    return input("Seleccione una opcion: ")

def main():
    while True:
        opcion = menu()
        
        if opcion == "1":
            mostrar_clientes()
        
        elif opcion == "2":
            registrar_cliente()
        
        elif opcion == "3":
            buscar_cliente()
        
        elif opcion == "4":
            actualizar_precio()
        
        elif opcion == "5":
            eliminar_cliente()
        
        elif opcion == "7":
            limpiar_pantalla()
            print("\nGracias por usar el sistema. ¡Hasta luego!")
            break
        
        else:
            limpiar_pantalla()
            print("Opcion no valida. Intente de nuevo.")
            pausar()

if __name__ == "__main__":
    main()

import os
from datos import clientes

# Funcion para limpiar pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Funcion para pausar y esperar que el usuario presione Enter
def pausar():
    input("\nPresione Enter para continuar...")

# 1. Mostrar todos los clientes
def mostrar_clientes():
    limpiar_pantalla()
    print("\n Lista de clientes:")
    if len(clientes) == 0:
        print("No hay clientes registrados.")
        pausar()
        return
    
    for cliente in clientes:
        print(f"ID: {cliente['id']} | Nombre: {cliente['nombre']} | Servicio: {cliente['servicio']} | Precio: ${cliente['precio']} | Visitas: {cliente['visitas']}")
    
    print(f"\nTotal de clientes: {len(clientes)}")
    pausar()

# 2. Registrar un nuevo cliente con validacion en bucle
def registrar_cliente():
    limpiar_pantalla()
    print("\n Registrar nuevo cliente\n")
    
    # Validacion ID (while)
    while True:
        id_cliente = input("ID del cliente: ")
        
        # Validar que no este vacio
        if not id_cliente or id_cliente.strip() == "":
            print("El ID no puede estar vacio.\n")
            continue
        
        # Verificar que el ID no exista en la lista
        id_existe = False
        for cliente in clientes:
            if cliente["id"] == id_cliente:
                id_existe = True
                break
        
        if id_existe:
            print(f"El ID '{id_cliente}' ya existe. Elija otro ID.\n")
            continue
        
        # Si llega aqui, el ID es valido y no existe
        print(f"ID '{id_cliente}' disponible. Continuando...\n")
        break
    
    # Validacion nombre (while)
    while True:
        nombre = input("Nombre: ")
        if not nombre or nombre.strip() == "":
            print("El nombre no puede estar vacio.\n")
            continue
        
        if len(nombre.strip()) < 2:
            print("El nombre debe tener al menos 2 caracteres.\n")
            continue
        
        break
    
    # Validacion servicio (while)
    while True:
        servicio = input("Servicio: ")
        if not servicio or servicio.strip() == "":
            print("El servicio no puede estar vacio.\n")
            continue
        
        if len(servicio.strip()) < 3:
            print("El servicio debe tener al menos 3 caracteres.\n")
            continue
        
        break
    
    # Validacion precio (while)
    while True:
        precio = input("Precio: ")
        if not precio or precio.strip() == "":
            print("El precio no puede estar vacio.\n")
            continue
        
        try:
            precio = float(precio)
            if precio <= 0:
                print("El precio debe ser mayor que 0.\n")
                continue
            break
        except ValueError:
            print("El precio debe ser un numero. No use letras.\n")
            continue
    
    # Validacion visitas (while)
    while True:
        visitas = input("Numero de visitas: ")
        if not visitas or visitas.strip() == "":
            print("Las visitas no pueden estar vacias.\n")
            continue
        
        try:
            visitas = int(visitas)
            if visitas < 0:
                print("Las visitas no pueden ser negativas.\n")
                continue
            break
        except ValueError:
            print("Las visitas deben ser un numero entero. No use letras.\n")
            continue
    
    # Si todas las validaciones pasan, se crea el nuevo cliente y se agrega a la lista
    nuevo_cliente = {
        "id": id_cliente,
        "nombre": nombre.strip(),
        "servicio": servicio.strip(),
        "precio": precio,
        "visitas": visitas
    }
    clientes.append(nuevo_cliente)
    print(f"\nCliente {nombre} registrado correctamente.")
    pausar()
    return True

# 3. Buscar cliente por ID
def buscar_cliente():
    limpiar_pantalla()
    print("\nBuscar Cliente\n")
    
    while True:
        id_cliente = input("Ingrese ID del cliente: ")
        if not id_cliente or id_cliente.strip() == "":
            print("El ID no puede estar vacio.\n")
            continue
        
        for cliente in clientes:
            if cliente["id"] == id_cliente:
                print("\nCliente encontrado:")
                print(f"ID: {cliente['id']}")
                print(f"Nombre: {cliente['nombre']}")
                print(f"Servicio: {cliente['servicio']}")
                print(f"Precio: ${cliente['precio']}")
                print(f"Visitas: {cliente['visitas']}")
                pausar()
                return cliente
        
        print(f"El ID '{id_cliente}' no corresponde a ningun cliente registrado.\n")

# 4. Actualizar precio de servicio
def actualizar_precio():
    limpiar_pantalla()
    print("\nActualizar Precio\n")
    
    # Validar ID del cliente (while)
    while True:
        id_cliente = input("Ingrese ID del cliente: ")
        if not id_cliente or id_cliente.strip() == "":
            print("El ID no puede estar vacio.\n")
            continue
        
        # Buascar cliente por ID
        cliente_encontrado = None
        for cliente in clientes:
            if cliente["id"] == id_cliente:
                cliente_encontrado = cliente
                break
        
        if cliente_encontrado is None:
            print(f"El ID '{id_cliente}' no corresponde a ningun cliente registrado.\n")
            continue
        
        break
    
    #Validar nuevo precio (while)
    while True:
        nuevo_precio = input("Nuevo precio: ")
        if not nuevo_precio or nuevo_precio.strip() == "":
            print("El precio no puede estar vacio.\n")
            continue
        
        try:
            nuevo_precio = float(nuevo_precio)
            if nuevo_precio <= 0:
                print("El precio debe ser mayor que 0.\n")
                continue
            break
        except ValueError:
            print("El precio debe ser un numero. No use letras.\n")
            continue
    
    # Actualizar el precio del cliente encontrado
    precio_anterior = cliente_encontrado["precio"]
    cliente_encontrado["precio"] = nuevo_precio
    print(f"\nPrecio actualizado para {cliente_encontrado['nombre']}: ${precio_anterior} -> ${nuevo_precio}")
    pausar()
    return True

# 5. Eliminar cliente
def eliminar_cliente():
    limpiar_pantalla()
    print("\nEliminar Cliente\n")
    
    while True:
        id_cliente = input("Ingrese ID del cliente a eliminar: ")
        if not id_cliente or id_cliente.strip() == "":
            print("El ID no puede estar vacio.\n")
            continue
        
        for cliente in clientes:
            if cliente["id"] == id_cliente:
                nombre_cliente = cliente["nombre"]
                clientes.remove(cliente)
                print(f"\nCliente {nombre_cliente} (ID: {id_cliente}) eliminado.")
                pausar()
                return True
        
        print(f"El ID '{id_cliente}' no corresponde a ningun cliente registrado.\n")
    
    pausar()

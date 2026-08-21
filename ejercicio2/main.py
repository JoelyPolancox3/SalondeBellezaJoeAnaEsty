from datos import inventario
from funciones import sumar_valores_diccionario


def main():
    print("Inventario:")

    for item, cantidad in inventario.items():
        print(item, ":", cantidad)

    total = sumar_valores_diccionario(inventario)

    print("La suma total de las cantidades disponibles es:", total)


main()
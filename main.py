from datos import inventario
from funciones import sumar_valores_diccionario

total= sumar_valores_diccionario(inventario)
print(f"La cantidad total de items disponibles en el inventario es: {total}")
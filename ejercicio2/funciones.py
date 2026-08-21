def sumar_valores_diccionario(diccionario):
    total = 0

    for valor in diccionario.values():
        if isinstance(valor, (int, float)):
            total += valor

    return total
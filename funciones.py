def sumar_valores_diccionario(diccionario) :
    suma_total = 0
    for valor in diccionario.values():
        if isinstance(valor,(int, float)):
            suma_total += valor
    return suma_total
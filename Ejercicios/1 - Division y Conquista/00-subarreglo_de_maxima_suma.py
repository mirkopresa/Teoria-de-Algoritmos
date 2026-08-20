# Dado un arreglo de n enteros (no olvidar que pueden haber números negativos),
# encontrar el subarreglo contiguo de máxima suma, utilizando División y Conquista.
# Indicar y justificar la complejidad del algoritmo.
# Ejemplos:
# [5, 3, 2, 4, -1] ->  [5, 3, 2, 4]
# [5, 3, -5, 4, -1] ->  [5, 3]
# [5, -4, 2, 4, -1] -> [5, -4, 2, 4]
# [5, -4, 2, 4] -> [5, -4, 2, 4]
# [-3, 4, -1, 2, 1, -5] -> [4, -1, 2, 1]


# A = 2, B = 2, C = 1, log en base 2 de 2 = 1, 1 = C -> O(n^c * log n) -> O(n*log(n))
def max_subarray(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    mitad = len(arr) // 2
    mitad_izq = max_subarray(arr[:mitad])
    mitad_der = max_subarray(arr[mitad:])
    cruzado = obtener_subarreglo_cruzado(arr)
    suma_max_izq = sum(mitad_izq)
    suma_max_der = sum(mitad_der)
    suma_max_cruzado = sum(cruzado)
    if suma_max_izq > suma_max_der and suma_max_izq > suma_max_cruzado:
        return mitad_izq
    elif suma_max_der > suma_max_izq and suma_max_der > suma_max_cruzado:
        return mitad_der
    else:
        return cruzado


def obtener_subarreglo_cruzado(arr: list[int]) -> list[int]:
    mitad = len(arr) // 2
    indice_izq = mitad
    suma_izq = 0
    suma = 0
    for i in range(mitad - 1, -1, -1):
        suma += arr[i]
        if suma > suma_izq:
            suma_izq = suma
            indice_izq = i
    indice_der = mitad
    suma_der = 0
    suma = 0
    for j in range(mitad, len(arr), 1):
        suma += arr[j]
        if suma > suma_der:
            suma_der = suma
            indice_der = j
    return arr[indice_izq : indice_der + 1]

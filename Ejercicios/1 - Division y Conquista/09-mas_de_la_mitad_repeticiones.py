# Implementar una función (que utilice división y conquista) de complejidad O(n log n) que dado un arreglo de n números enteros devuelva true o false
# según si existe algún elemento que aparezca más de la mitad de las veces. Justificar el orden de la solución.
# Ejemplos:
# [1, 2, 1, 2, 3] -> false
# [1, 1, 2, 3] -> false
# [1, 2, 3, 1, 1, 1] -> true
# [1] -> true


def mas_de_la_mitad(arr: list[int]) -> bool:
    return dividir(arr) != None


def dividir(arr: list[int]) -> int | None:
    if len(arr) <= 1:
        return arr[0]
    mitad = len(arr) // 2
    ganador_izq = mas_de_la_mitad(arr[:mitad])
    ganador_der = mas_de_la_mitad(arr[mitad:])
    return contar(arr, ganador_izq, ganador_der)


def contar(arr: list[int], ganador_izq: int, ganador_der: int) -> int | None:
    contador_1 = 0
    contador_2 = 0
    for num in arr:
        if num == ganador_izq:
            contador_1 += 1
        if num == ganador_der:
            contador_2 += 1
    mitad = len(arr) // 2
    if contador_1 > mitad:
        return ganador_izq
    elif contador_2 > mitad:
        return ganador_der
    return None


print(mas_de_la_mitad([1, 2, 3, 1]))

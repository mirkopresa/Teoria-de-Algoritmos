# Se cuenta con un arreglo de enteros ordenado de manera ascendente que contiene exactamente un número duplicado
# (es decir, todos los demás elementos son distintos, sin duplicados).
# Implementar una función que encuentre dicho número utilizando división y conquista.
# Indicar y justificar la complejidad del algoritmo, utilizando el Teorema Maestro.


def elemento_duplicado(arr: list[int]) -> int | None:
    return duplicado_recursivo(arr, 0, len(arr) - 1)


# A = 2, B = 2, C = 0 -> log en base 2 de 2 = 1 -> 1 > C -> O(n^c) -> O(n)
# None para incluir arreglos con numeros negativos
def duplicado_recursivo(arr: list[int], inicio: int, fin: int) -> int | None:
    if inicio >= fin:
        return None
    mitad = (inicio + fin) // 2
    if arr[mitad] == arr[mitad + 1]:
        return arr[mitad]
    mitadIzq = duplicado_recursivo(arr, inicio, mitad)
    if mitadIzq == None:
        return duplicado_recursivo(arr, mitad + 1, fin)
    return mitadIzq

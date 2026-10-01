# Implementar una función que, dado un arreglo ordenado y sin repetidos de valores enteros no negativos, obtenga el mínimo
# valor que no se encuentre en el arreglo. Indicar y justificar adecuadamente la complejidad del algoritmo.
# Por ejemplo:
# minimoExcluido([0, 1, 5]) --> 2
# minimoExcluido([1, 3, 5]) --> 0
# minimoExcluido([0, 1, 2, 3, 4, 5]) --> 6
# minimoExcluido([0, 1, 2, 3, 4, 5, 1234567]) --> 6


def minimo_excluido(arr: list[int]) -> int:
    return minimo_rec(arr, 0, len(arr) - 1)


def minimo_rec(arr: list[int], inicio: int, fin: int) -> int:
    if inicio > fin:
        return inicio
    mitad = (inicio + fin) // 2
    if arr[mitad] == mitad:
        return minimo_rec(arr, mitad + 1, fin)
    return minimo_rec(arr, inicio, mitad - 1)


print(minimo_excluido([0, 1, 2, 3, 4, 5, 1234567]))

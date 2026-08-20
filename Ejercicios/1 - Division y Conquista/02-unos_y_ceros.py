# Se tiene un arreglo tal que [1, 1, 1, …, 0, 0, …] (es decir, unos seguidos de ceros).
# Se pide una función de complejidad O(log(n)) que encuentre el índice del primer 0.
# Si no hay ningún 0 (solo hay unos), debe devolver -1.


def indice_primer_cero(arr: list[int]) -> int:
    if len(arr) == 0 or arr[len(arr) - 1] == 1:
        return -1
    return indice_recursivo(arr, 0, len(arr) - 1)


# A = 1, B = 2, C = 0 -> log en base 2 de 1 = 0, 0 = C, entonces O(n^c * log(n)) -> O(log n)
def indice_recursivo(arr: list[int], inicio: int, fin: int) -> int:
    if inicio == fin:
        return inicio
    mitad = (inicio + fin) // 2
    if arr[mitad] == 1:
        return indice_recursivo(arr, mitad + 1, fin)
    else:
        return indice_recursivo(arr, inicio, mitad)

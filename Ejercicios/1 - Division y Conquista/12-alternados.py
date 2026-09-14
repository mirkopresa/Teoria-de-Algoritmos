# Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn},
# tal que la cantidad total de elementos del arreglo  es potencia de 2 (por ende, n también lo es).
# Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que quede con la forma
# {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, sin utilizar espacio adicional (obviando el utilizado por la recursividad y variables de tipos simples).
# ¿Cual es la complejidad del algoritmo?


def alternar(arr: list) -> None:
    return alternar_rec(arr, 0, len(arr) - 1)


def alternar_rec(arr: list, inicio: int, fin: int) -> None:
    if fin - inicio + 1 == 2:
        return
    if fin - inicio + 1 == 4:
        arr[inicio + 1], arr[inicio + 2] = arr[inicio + 2], arr[inicio + 1]
        return
    mitad = (inicio + fin) // 2
    alternar_rec(arr, inicio, mitad)
    alternar_rec(arr, mitad + 1, fin)
    for i in range(1, mitad - inicio + 1, 2):
        arr[inicio + i], arr[mitad + i] = arr[mitad + i], arr[inicio + i]

# Implementar una función, que utilice división y conquista, de complejidad O(n) que dado un arreglo de nn números enteros
# devuelva true o false según si existe algún elemento que aparezca más de dos tercios de las veces.
# Justificar la complejidad de la solución.


def mas_de_dos_tercios(arr: list[int]) -> bool:
    posible_repetido = mas_de_dos_tercios_rec(arr)
    return posible_repetido is not None


def mas_de_dos_tercios_rec(arr: list[int]) -> int | None:
    if len(arr) == 1:
        return arr[0]

    nuevo = []
    for i in range(0, len(arr) - 2, 3):
        if arr[i] == arr[i + 1] and arr[i] == arr[i + 2]:
            nuevo.append(arr[i])

    posible_repetido = mas_de_dos_tercios_rec(nuevo) if nuevo != [] else None
    if posible_repetido is not None and arr.count(posible_repetido) > len(arr) // 3 * 2:
        return posible_repetido
    if len(arr) % 3 != 0:
        if arr.count(arr[len(arr) - 2]) > len(arr) // 3 * 2:
            return arr[len(arr) - 2]
        if arr.count(arr[-1]) > len(arr) // 3 * 2:
            return arr[-1]
    return None

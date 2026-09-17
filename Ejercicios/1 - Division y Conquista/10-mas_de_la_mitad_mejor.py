# Resolver el ejercicio anterior, por división y conquista, en complejidad O(n)O(n), dada la misma aclaración.
# Justificar la complejidad de la solución.


def mas_de_la_mitad(arr: list[int]) -> bool:
    posible_repetido = mas_de_la_mitad_rec(arr)
    return posible_repetido is not None


def mas_de_la_mitad_rec(arr: list[int]) -> int | None:
    if len(arr) == 1:
        return arr[0]

    nuevo: list[int] = []
    for i in range(0, len(arr) - 1, 2):
        if arr[i] == arr[i + 1]:
            nuevo.append(arr[i])

    posible_repetido = mas_de_la_mitad_rec(nuevo) if nuevo != [] else None
    if posible_repetido is not None and arr.count(posible_repetido) > len(arr) // 2:
        return posible_repetido
    if len(arr) % 2 != 0 and arr.count(arr[-1]) > len(arr) // 2:
        return arr[-1]
    return None

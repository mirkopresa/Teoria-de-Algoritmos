# Implementar Merge Sort. Justificar la complejidad del algoritmo mediante el teorema maestro.


# A = 2, B = 2, C = 1, log en base 2 de 2 = 1, 1 = C -> O(n^c * log n) -> O(n*log(n))
def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    mitad = len(arr) // 2
    mitad_izq = merge_sort(arr[:mitad])
    mitad_der = merge_sort(arr[mitad:])
    return merge(mitad_izq, mitad_der)


def merge(izq: list[int], der: list[int]) -> list[int]:
    resultado = []
    i, j = 0, 0
    while i < len(izq) and j < len(der):
        if izq[i] >= der[j]:
            resultado.append(der[j])
            j += 1
        else:
            resultado.append(izq[i])
            i += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

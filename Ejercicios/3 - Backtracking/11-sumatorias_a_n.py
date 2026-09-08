# Escribir un algoritmo que, utilizando backtracking, dada una lista de enteros positivos L y un entero n
# devuelva todos los subconjuntos de L que suman exactamente n.


def sumatorias_n(lista: list[int], n: int) -> list[list[int]]:
    return sumatorias_rec(lista, n, 0, [], ([], 0))


def sumatorias_rec(
    lista: list[int],
    n: int,
    indice: int,
    soluciones: list[list[int]],
    solucion: tuple[list[int], int],
) -> list[list[int]]:
    if indice == len(lista):
        return soluciones

    resultado, suma_parcial = solucion

    if lista[indice] + suma_parcial <= n:
        resultado.append(lista[indice])
        if lista[indice] + suma_parcial == n:
            soluciones.append(resultado[:])
        suma_parcial += lista[indice]
        _ = sumatorias_rec(lista, n, indice + 1, soluciones, (resultado, suma_parcial))
        resultado.pop()
        suma_parcial -= lista[indice]
    return sumatorias_rec(lista, n, indice + 1, soluciones, (resultado, suma_parcial))


print(sumatorias_n([1, 2, 3, 4, 5], 6))

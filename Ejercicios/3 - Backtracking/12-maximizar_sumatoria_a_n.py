# Modificar el algoritmo anterior para que, dada una lista de enteros positivos L y un entero n,
# devuelva un subconjunto de L que sume exactamente n, o, en caso de no existir,
# que devuelva el subconjunto de suma máxima sin superar el valor de n.


def max_sumatoria_n(lista: list[int], n: int) -> list[int]:
    solucion, _ = sumatoria_rec(lista, n, 0, ([], 0), ([], 0))
    return solucion


def sumatoria_rec(
    lista: list[int],
    n: int,
    indice: int,
    solucion: tuple[list[int], int],
    solucion_optima: tuple[list[int], int],
) -> tuple[list[int], int]:
    sol_parcial, suma_parcial = solucion
    sol_optima, suma_optima = solucion_optima
    if suma_parcial > suma_optima:
        solucion_optima = (sol_parcial[:], suma_parcial)
    if indice == len(lista):
        return solucion_optima
    if suma_parcial + lista[indice] <= n:
        sol_parcial.append(lista[indice])
        suma_parcial += lista[indice]
        if suma_parcial == n:
            res = (sol_parcial[:], suma_parcial)
            sol_parcial.pop()
            suma_parcial -= lista[indice]
            return res
        solucion_optima = sumatoria_rec(
            lista,
            n,
            indice + 1,
            (sol_parcial, suma_parcial),
            solucion_optima,
        )
        sol_parcial.pop()
        suma_parcial -= lista[indice]
    return sumatoria_rec(
        lista, n, indice + 1, (sol_parcial, suma_parcial), solucion_optima
    )


print(max_sumatoria_n([1, 2, 20, 4, 1, 9, 4, 7, 1, 20], 10))

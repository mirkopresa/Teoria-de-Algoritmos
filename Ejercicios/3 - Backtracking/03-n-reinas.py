# Dado un tablero de ajedrez n x n, implementar un algoritmo por backtracking que ubique (si es posible) a n reinas
# de tal manera que ninguna pueda comerse con ninguna.


def nreinas(n: int) -> list[tuple[int, int]]:
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    return nreinas_rec(matriz, n, [], 0)


def nreinas_rec(matriz: list[list[int]], n: int, reinas: list[tuple[int, int]], f_actual: int) -> list[tuple[int, int]]:
    if f_actual == n:
        return reinas if len(reinas) == n else []

    for i in range(len(matriz)):
        if es_compatible(matriz, f_actual, i):
            reinas.append((f_actual, i))
            matriz[f_actual][i] = 1
            res = nreinas_rec(matriz, n, reinas, f_actual + 1)
            if res != []:
                return res
            reinas.pop()
            matriz[f_actual][i] = 0
    return []


def es_compatible(matriz: list[list[int]], f_actual: int, c_actual: int) -> bool:
    i = 0
    while i < f_actual:
        if matriz[i][c_actual] == 1:
            return False
        i += 1
    i, j = f_actual - 1, c_actual - 1
    while i >= 0 and j >= 0:
        if matriz[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = f_actual - 1, c_actual + 1
    while i >= 0 and j < len(matriz):
        if matriz[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

# Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer,
# y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i]
# contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se trata de un restaurante familiar,
# las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse.
# Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan la mayor cantidad
# de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos).
# Indicar y justificar la complejidad del algoritmo.

# Casos base
# n = 0 -> []
# n = 1 -> si P[0] <= W: [P[0]] else []

# Ecuacion de recurrencia
# OPT[i, W] = max(OPT[i-1, W], OPT[i-1, W-P[i-1]] + P[i-1])
def bodegon_dinamico(P: list[int], W: int) -> list[int]:
    if len(P) == 0:
        return []
    if len(P) == 1:
        if P[0] <= W:
            return [P[0]]
        return []
    matriz_optimos = [[0] * (W + 1) for _ in range(len(P) + 1)]
    for i in range(1, len(P) + 1):
        for j in range(1, W + 1):
            if P[i - 1] <= j:
                matriz_optimos[i][j] = max(matriz_optimos[i - 1][j], matriz_optimos[i - 1][j - P[i - 1]] + P[i - 1])
            else:
                matriz_optimos[i][j] = matriz_optimos[i - 1][j]
    return reconstruir(matriz_optimos, P, W)


def reconstruir(matriz_optimos: list[list[int]], P: list[int], indice_j: int) -> list[int]:
    res = []
    i, j = len(P), indice_j
    while i > 0 and j >= 0:
        if matriz_optimos[i][j] != matriz_optimos[i - 1][j]:
            res.append(P[i - 1])
            j -= P[i - 1]
        i -= 1
    return res[::-1]


print(bodegon_dinamico([1, 4, 7], 8))

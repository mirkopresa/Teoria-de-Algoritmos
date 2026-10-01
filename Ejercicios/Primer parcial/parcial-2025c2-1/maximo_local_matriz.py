# Sea A una matríz de n x n (con n ≥3) con todos valores diferentes. Definimos la vecindad de una celda como las 8 celdas vecinas
# (arriba, abajo, derecha, izquierda, y las 4 diagonales), siempre que existan (en los bordes algunas no existirán). Un elemento A[i, j] es
# un máximo local si su valor es estrictamente mayor que el valor de todas las celdas vecinas. Implementar un algoritmo de división y
# conquista que encuentre un máximo local en tiempo O(n). Justificar adecuadamente la complejidad del algoritmo implementado.


def obtener_maximo_local(matriz: list[list[int]]) -> int:
    n = len(matriz)
    return maximo_local(matriz, 0, 0, n - 1, n - 1)


def maximo_local(matriz: list[list[int]], inicio_fila: int, inicio_columna: int, fin_fila: int, fin_columna: int) -> int:
    fila_max, columna_max, elem_max = 0, 0, matriz[0][0]
    for i in range(inicio_fila, fin_fila + 1):
        fila_sup, columna_sup, es_maximo_sup = revisar_vecinos(matriz, 0, i)
        if es_maximo_sup:
            return matriz[fila_sup][columna_sup]
        if matriz[fila_sup][columna_sup] > elem_max:
            fila_max, columna_max, elem_max = fila_sup, columna_sup, matriz[fila_sup][columna_sup]
        fila_inf, columna_inf, es_maximo_inf = revisar_vecinos(matriz, fin_fila - 1, i)
        if es_maximo_inf:
            return matriz[fila_inf][columna_inf]
        if matriz[fila_inf][columna_inf] > elem_max:
            fila_max, columna_max, elem_max = fila_inf, columna_inf, matriz[fila_inf][columna_inf]
    for i in range(inicio_columna, fin_columna + 1):
        fila_izq, columna_izq, es_maximo_izq = revisar_vecinos(matriz, i, 0)
        if es_maximo_izq:
            return matriz[fila_izq][columna_izq]
        if matriz[fila_izq][columna_izq] > elem_max:
            fila_max, columna_max, elem_max = fila_izq, columna_izq, matriz[fila_izq][columna_izq]
        fila_der, columna_der, es_maximo_der = revisar_vecinos(matriz, i, fin_columna - 1)
        if es_maximo_der:
            return matriz[fila_der][columna_der]
        if matriz[fila_der][columna_der] > elem_max:
            fila_max, columna_max, elem_max = fila_der, columna_der, matriz[fila_der][columna_der]
    mitad_fila = (inicio_fila + fin_fila) // 2
    mitad_columna = (inicio_columna + fin_columna) // 2
    for i in range(inicio_fila, fin_fila + 1):
        fila_h, columna_h, es_maximo_h = revisar_vecinos(matriz, mitad_fila, i)
        if es_maximo_h:
            return matriz[fila_h][columna_h]
        if matriz[fila_h][columna_h] > elem_max:
            fila_max, columna_max, elem_max = fila_h, columna_h, matriz[fila_h][columna_h]
    for i in range(inicio_columna, fin_columna + 1):
        fila_v, columna_v, es_maximo_v = revisar_vecinos(matriz, i, mitad_columna)
        if es_maximo_v:
            return matriz[fila_v][columna_v]
        if matriz[fila_v][columna_v] > elem_max:
            fila_max, columna_max, elem_max = fila_v, columna_v, matriz[fila_v][columna_v]
    inicio_fila_nuevo, inicio_columna_nuevo, fin_fila_nuevo, fin_columna_nuevo = 0, 0, 0, 0
    if fila_max < mitad_fila and columna_max < mitad_columna:
        inicio_fila_nuevo = fila_max
        fin_fila_nuevo = mitad_fila - 1
        inicio_columna_nuevo = columna_max
        fin_columna_nuevo = mitad_columna - 1
    elif fila_max < mitad_fila and columna_max > mitad_columna:
        inicio_fila_nuevo = fila_max
        fin_fila_nuevo = mitad_fila - 1
        inicio_columna_nuevo = mitad_columna + 1
        fin_columna_nuevo = columna_max
    elif fila_max > mitad_fila and columna_max < mitad_columna:
        inicio_fila_nuevo = mitad_fila + 1
        fin_fila_nuevo = fila_max
        inicio_columna_nuevo = columna_max
        fin_columna_nuevo = mitad_columna - 1
    else:
        inicio_fila_nuevo = mitad_fila + 1
        fin_fila_nuevo = fila_max
        inicio_columna_nuevo = mitad_columna + 1
        fin_columna_nuevo = columna_max
    return maximo_local(matriz, inicio_fila_nuevo, inicio_columna_nuevo, fin_fila_nuevo, fin_columna_nuevo)


def revisar_vecinos(matriz: list[list[int]], fila: int, columna: int) -> tuple[int, int, bool]:
    es_maximo = True
    maximo_fila, maximo_columna = fila, columna
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            indice_fila = fila + i
            indice_columna = columna + j
            if indice_fila < 0 or indice_fila > len(matriz) - 1:
                continue
            if indice_columna < 0 or indice_columna > len(matriz) - 1:
                continue
            if matriz[indice_fila][indice_columna] > matriz[maximo_fila][maximo_columna]:
                es_maximo = False
                maximo_fila, maximo_columna = indice_fila, indice_columna
    return maximo_fila, maximo_columna, es_maximo


# el peor ejercicio que vi en mi vida

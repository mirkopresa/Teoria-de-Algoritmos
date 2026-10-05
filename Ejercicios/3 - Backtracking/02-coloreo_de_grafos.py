# Implementar un algoritmo que reciba un grafo y un número n que, utilizando backtracking, indique si es posible pintar
# cada vértice con n colores de tal forma que no hayan dos vértices adyacentes con el mismo color.


from grafo import Grafo


def colorear(grafo: Grafo, n: int) -> bool:
    if n < len(grafo):
        return False
    return colorear_bt(grafo, grafo.obtener_vertices(), n, 0, {})


def colorear_bt(grafo: Grafo, vertices: list, n: int, indice: int, colores: dict) -> bool:
    if len(colores) == len(vertices):
        return True
    v = vertices[indice]
    for i in range(n):
        colores[v] = i
        if not es_compatible(grafo, v, colores):
            continue
        if colorear_bt(grafo, vertices, n, indice + 1, colores):
            return True
        del colores[v]
    return False


def es_compatible(grafo: Grafo, v, colores: dict) -> bool:
    for w in grafo.adyacentes(v):
        if w in colores and colores[w] == colores[v]:
            return False
    return True

# Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un máximo Independent Set del mismo.


def independent_set(grafo):
    return independent_set_rec(grafo, grafo.obtener_vertices(), 0, [])


def independent_set_rec(grafo, vertices: list, indice: int, camino: list) -> list:
    if indice == len(grafo):
        return camino[:]
    v_actual = vertices[indice]
    res1 = []
    if es_compatible(grafo, v_actual, camino):
        camino.append(v_actual)
        res1 = independent_set_rec(grafo, vertices, indice + 1, camino)
        camino.pop()
    res2 = independent_set_rec(grafo, vertices, indice + 1, camino)
    return res1 if len(res1) > len(res2) else res2


def es_compatible(grafo, v, camino):
    for w in camino:
        if grafo.estan_unidos(v, w):
            return False
    return True

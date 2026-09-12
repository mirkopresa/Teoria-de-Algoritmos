# Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al
# menos uno de sus extremos en dicho conjunto. Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover.

# Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo.


def vertex_cover_min(grafo):
    vertices_independientes = set(independent_set(grafo))
    resultado = []
    for v in grafo:
        if v not in vertices_independientes:
            resultado.append(v)
    return resultado


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

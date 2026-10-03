# Implementar un algoritmo que, dado un grafo no dirigido, obtenga el clique de mayor tamaño dentro del mismo
# (utilizando backtracking).


def clique_maximo(grafo) -> list:
    return list(clique_bt(grafo, grafo.obtener_vertices(), 0, set(), set()))


def clique_bt(grafo, vertices: list, indice: int, solucion_parcial: set, solucion_optima: set) -> set:
    if len(solucion_parcial) > len(solucion_optima):
        solucion_optima = solucion_parcial.copy()
    if indice == len(vertices):
        return solucion_optima
    if len(vertices) - indice + len(solucion_parcial) <= len(solucion_optima):
        return solucion_optima
    v = vertices[indice]
    if es_compatible(grafo, v, solucion_parcial):
        solucion_parcial.add(v)
        solucion_optima = clique_bt(grafo, vertices, indice + 1, solucion_parcial, solucion_optima)
        solucion_parcial.remove(v)
    return clique_bt(grafo, vertices, indice + 1, solucion_parcial, solucion_optima)


def es_compatible(grafo, nuevo, solucion_parcial: set) -> bool:
    for v in solucion_parcial:
        if not grafo.estan_unidos(nuevo, v):
            return False
    return True

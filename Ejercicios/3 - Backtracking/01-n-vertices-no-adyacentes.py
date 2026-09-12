# Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a #V,
# devuelva si es posible obtener un subconjunto de n vertices tal que ningun par de vertices sea adyacente entre si.


def no_adyacentes(grafo, n: int) -> list | None:
    return no_adyacentes_recursivo(grafo, n, grafo.obtener_vertices(), 0, [])


def no_adyacentes_recursivo(grafo, n: int, vertices: list, indice: int, camino: list) -> list | None:
    if len(camino) == n:
        return camino[:]
    if indice == len(grafo) or no_alcanza(indice, vertices, n):
        return None
    v_actual = vertices[indice]
    if es_compatible(grafo, v_actual, camino):
        camino.append(v_actual)
        solucion = no_adyacentes_recursivo(grafo, n, vertices, indice + 1, camino)
        if solucion is not None:
            return solucion
        camino.pop()
    return no_adyacentes_recursivo(grafo, n, vertices, indice + 1, camino)


def es_compatible(grafo, v: int, camino: list) -> bool:
    for w in camino:
        if grafo.estan_unidos(v, w):
            return False
    return True


def no_alcanza(indice: int, vertices: list, n: int) -> bool:
    return len(vertices) - indice < n

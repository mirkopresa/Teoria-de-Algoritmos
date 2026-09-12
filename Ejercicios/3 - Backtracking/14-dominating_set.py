# Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G: o bien

# (i) pertenece a D;
# o bien (ii) es adyacente a un vértice en D.

# Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con la mínima cantidad de vértices.


def dominating_set_min(grafo) -> list:
    return dominating_rec(
        grafo,
        grafo.obtener_vertices(),
        0,
        [],
        set(grafo.obtener_vertices()),
        grafo.obtener_vertices(),
    )


def dominating_rec(
    grafo,
    vertices: list,
    indice: int,
    solucion: list,
    vertices_no_cubiertos: set,
    solucion_optima: list,
) -> list:
    # Poda
    if len(solucion) >= len(solucion_optima):
        return solucion_optima

    if indice == len(vertices):
        if len(vertices_no_cubiertos) == 0:
            solucion_optima = solucion[:]
        return solucion_optima

    v_actual = vertices[indice]
    cubiertos = []
    # Caso 1 - Agrego al vertice actual como dominante y lo elimino en los cubiertos, junto a sus adyacentes
    if v_actual in vertices_no_cubiertos:
        vertices_no_cubiertos.remove(v_actual)
        cubiertos.append(v_actual)
    for w in grafo.adyacentes(v_actual):
        if w in vertices_no_cubiertos:
            vertices_no_cubiertos.remove(w)
            cubiertos.append(w)
    solucion.append(v_actual)
    solucion_optima = dominating_rec(
        grafo, vertices, indice + 1, solucion, vertices_no_cubiertos, solucion_optima
    )
    # Caso 2 - No lo tenemos en cuenta
    for u in cubiertos:
        vertices_no_cubiertos.add(u)
    solucion.pop()
    return dominating_rec(
        grafo, vertices, indice + 1, solucion, vertices_no_cubiertos, solucion_optima
    )

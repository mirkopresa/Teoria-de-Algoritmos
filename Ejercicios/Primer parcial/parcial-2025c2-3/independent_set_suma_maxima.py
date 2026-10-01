# Sea G un grafo dirigido “camino” (las aristas son de la forma (vi, vi+1)). Cada vertice tiene un valor (positivo). Implementar un
# algoritmo que, utilizando programación dinámica, obtenga el Set Independiente de suma máxima dentro de un grafo de dichas
# características. También escribir el algoritmo que permita reconstruir la solución. Indicar y justificar la complejidad del algoritmo
# implementado (el de programación dinámica, y también el de la reconstrucción).

# Juan el vago 2.0
# Ecuacion de recurrencia: optimos[i] = max(vertices[i] + optimos[i - 2], optimos[i - 1])
# Casos bases: 1 vertice -> optimos[0] = vertices[0], 2 vertices -> optimos[1] = max(vertices[0], vertices[1])

# O(n) porque iteramos todos los vertices haciendo operaciones O(1)
def max_sum(grafo) -> list[int]:
    vertices = grafo.obtener_vertices()
    if len(vertices) == 0:
        return []
    if len(vertices) == 1:
        return [vertices[0]]
    if len(vertices) == 2:
        max(vertices[0], vertices[1])
    optimos = [0] * len(vertices)
    optimos[0] = vertices[0]
    optimos[1] = max(vertices[0], vertices[1])
    for i in range(2, len(vertices)):
        optimos[i] = max(vertices[i] + optimos[i - 2], optimos[i - 1])
    return reconstruccion(optimos, vertices)


def reconstruccion(optimos: list[int], vertices: list[int]) -> list[int]:
    resultado = []
    i = len(vertices) - 1
    while i >= 0:
        if i == 0:
            resultado.append(vertices[i])
            break
        if optimos[i] == optimos[i - 1]:
            i -= 1
        else:
            resultado.append(vertices[i])
            i -= 2
    return resultado[::-1]


# SOY UN PAJERO ERA POR PD E HICE BT
"""
def max_sum_independent_set(grafo) -> list[int]:
    res, _ = max_sum_grafo(grafo, grafo.obtener_vertices(), 0, (set(), 0), (set(), 0))
    return list(res)


def max_sum_grafo(grafo, vertices: list[int], indice: int, solucion_optima: tuple[set, int], solucion_parcial: tuple[set, int]) -> tuple[set, int]:
    _, suma_optima = solucion_optima
    res_parcial, suma_parcial = solucion_parcial
    if suma_parcial > suma_optima:
        solucion_optima = (res_parcial.copy(), suma_parcial)
    if indice == len(vertices):
        return solucion_optima
    v = vertices[indice]
    if es_compatible(grafo, res_parcial, v):
        res_parcial.add(v)
        suma_parcial += v
        solucion_optima = max_sum_grafo(grafo, vertices, indice + 1, solucion_optima, (res_parcial, suma_parcial))
        res_parcial.remove(v)
        suma_parcial -= v
    return max_sum_grafo(grafo, vertices, indice + 1, solucion_optima, (res_parcial, suma_parcial))


def es_compatible(grafo, solucion_parcial: set, v: int) -> bool:
    for w in grafo.adyacentes(v):
        if w in solucion_parcial:
            return False
    return True
"""

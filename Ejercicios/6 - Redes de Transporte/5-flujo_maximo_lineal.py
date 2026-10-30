# Dado un flujo máximo de un grafo, implementar un algoritmo que, si se le aumenta en una unidad la capacidad a una arista
# (por ejemplo, a una arista de capacidad 3 se le aumenta a 4), permita obtener el nuevo flujo máximo en tiempo lineal en vértices y aristas.
# Indicar y justificar la complejidad del algoritmo implementado.

from collections import deque

from grafo import Grafo


# O(V + E)
def aumentar_flujo_maximo(grafo: Grafo, s, t, flujos: dict, arista: tuple) -> dict:
    red_residual = construir_red_residual(grafo, flujos)
    v_aumento, w_aumento = arista
    if red_residual.estan_unidos(v_aumento, w_aumento):
        return flujos
    red_residual.agregar_arista(v_aumento, w_aumento, 1)
    visitados = set()
    visitados.add(s)
    cola = deque()
    cola.append(s)
    padres = {s: None}
    while cola:
        v = cola.popleft()
        if v == t:
            # Se pudo llegar al sumidero, existe un camino que aumenta el flujo
            return reconstruir_flujo(padres, flujos, s, t)
        for w in red_residual.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                cola.append(w)
                padres[w] = v
    return flujos


# O(V) a lo sumo
def reconstruir_flujo(padres: dict, flujos: dict, t) -> dict:
    camino = []
    actual = t
    while actual is not None:
        camino.append(actual)
        actual = padres[actual]
    camino.reverse()
    flujos_nuevos = flujos.copy()
    for i in range(len(camino) - 1):
        v, w = camino[i], camino[i + 1]
        if (v, w) in flujos_nuevos:
            flujos_nuevos[(v, w)] += 1
    return flujos_nuevos


# O(V + E)
def construir_red_residual(grafo: Grafo, flujos: dict) -> Grafo:
    red_residual = Grafo(es_dirigido=True, vertices_init=grafo.obtener_vertices())
    for v in grafo:
        for w in grafo.adyacentes(v):
            flujo = flujos[(v, w)]
            peso_original = grafo.peso_arista(v, w)
            if peso_original > flujo:
                red_residual.agregar_arista(v, w, peso_original - flujo)
            if flujo > 0:
                red_residual.agregar_arista(w, v, flujo)
    return red_residual

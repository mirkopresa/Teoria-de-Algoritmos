# Dado un grafo bipartito no dirigido, un match es un subconjunto de las aristas en el cual para todo vértice V a lo sumo una
# arista del match incide en V (en el match, tienen grado a lo sumo 1).
# Decimos que el vértice V está matcheado si hay alguna arista que incida en él (sino, está unmatcheado).
# El matching máximo es aquel en el que tenemos la mayor cantidad de aristas (matcheamos la mayor cantidad posible).
# Dar una metodología para encontrar el matching máximo de un grafo, explicando en detalle cómo se modela el problema,
# cómo se lo resuelve y cómo se consigue el matching máximo.
# ¿Cuál es el orden temporal de la solución implementada?

from collections import deque

import ff as flujo
from grafo import Grafo


def matching_maximo(grafo: Grafo) -> list:
    grafo_flujo, s, t = crear_grafo_flujo(grafo)
    flujos = flujo(grafo_flujo, s, t)  # type: ignore hacer de cuenta que esta implementado FF
    resultado = []
    for adyacente in grafo_flujo.adyacentes(t):
        if flujos[(adyacente, t)] == 1:
            for w in grafo_flujo.adyacentes(adyacente):
                if flujos[(w, adyacente)] == 1:
                    resultado.append((w, adyacente))
    return resultado


def crear_grafo_flujo(grafo: Grafo) -> tuple[Grafo, str, str]:
    grafo = Grafo(es_dirigido=True, vertices_init=grafo.obtener_vertices())
    super_fuente = "super_fuente"
    super_sumidero = "super_sumidero"
    grafo.agregar_vertice(super_fuente)
    grafo.agregar_vertice(super_sumidero)
    aleatorio = grafo.vertice_aleatorio()
    orden = bfs(grafo, aleatorio)
    visitados = set()
    for v in grafo:
        for w in grafo.adyacentes(v):
            if w not in visitados:
                if orden[v] == 0:
                    grafo.agregar_arista(v, w, 1)
                else:
                    grafo.agregar_arista(w, v, 1)
        visitados.add(v)
    for v in grafo:
        if orden[v] == 0:
            grafo.agregar_arista("super_fuente", v, 1)
        else:
            grafo.agregar_arista(v, "super_sumidero", 1)
    return grafo, super_fuente, super_sumidero


def bfs(grafo: Grafo, origen: str) -> dict:
    orden = {origen: 0}
    visitados = set()
    visitados.add(origen)
    cola = deque()
    cola.append(origen)
    while cola:
        v = cola.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                orden[w] = 1 - orden[v]
                cola.append(w)
                visitados.add(w)
    return orden

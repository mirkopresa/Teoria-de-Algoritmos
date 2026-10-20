# Decimos que dos caminos son disjuntos si no comparten aristas (pueden compartir nodos).
# Dado un grafo dirigido y dos vértices s y t, encontrar el máximo número de caminos disjuntos s-t en G.
# Dar una metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se consigue el máximo número de caminos disjuntos.
# ¿Cuál es la complejidad temporal de la solución implementada? ¿Cómo resolverías el problema si el grafo fuera no dirigido?

# Considerar que la función flujo(red) que implementa el algoritmo de Ford-Fulkerson (usando BFS, definida por Edmonds y Karp)
# ya se encuentra implementada, y devuelve un diccionario con la asignación de flujo que pasa por cada arista de la red definida.

# La función flujo recibe la red de transporte (debe cumplir con las propiedades de red de transporte), la fuente y el sumidero, en ese orden.
# Devuelve un diccionario Arista -> flujo.

from collections import deque

from ff import flujo
from grafo import Grafo


# Se modela el problema de manera que se crea un nuevo grafo con aristas dirigidas de peso 1, y se obtiene el flujo del grafo.
# Por cada camino desde la fuente, vamos a recorrerlo hasta el sumidero y anularemos ese camino (le ponemos flujo 0)
def disjuntos(grafo: Grafo, s, t) -> list:
    # devolver una lista en la cual cada elemento es una lista, con el camino
    # entre s y t. Todos esos caminos deben incluir inicio (s) y fin (t).
    grafo_con_pesos = Grafo(es_dirigido=True, vertices_init=grafo.obtener_vertices())
    for v in grafo:
        for w in grafo.adyacentes(v):
            grafo_con_pesos.agregar_arista(v, w, 1)
    flujos = flujo(grafo_con_pesos, s, t)
    caminos = []
    camino_actual = bfs(grafo, s, t, flujos)
    while camino_actual is not None:
        caminos.append(camino_actual)
        for i in range(1, len(camino_actual)):
            v, w = camino_actual[i - 1], camino_actual[i]
            flujos[(v, w)] = 0
        camino_actual = bfs(grafo, s, t, flujos)
    return caminos


def bfs(grafo: Grafo, origen, destino, flujo: dict) -> list | None:
    visitados = set()
    visitados.add(origen)
    padres = {origen: None}
    cola = deque()
    cola.append(origen)
    while cola:
        v = cola.popleft()
        if v == destino:
            break
        for w in grafo.adyacentes(v):
            if w not in visitados and flujo[(v, w)] > 0:
                visitados.add(w)
                padres[w] = v
                cola.append(w)
    return reconstruir_camino(destino, padres)


def reconstruir_camino(destino, padres: dict) -> list | None:
    if destino not in padres:
        return None
    actual = destino
    camino = []
    while actual is not None:
        camino.append(actual)
        actual = padres[actual]
    return camino[::-1]

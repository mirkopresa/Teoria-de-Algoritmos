# Implementar el algoritmo de Ford-Fulkerson, asumiendo que ya está implementada una función actualizar_grafo_residual,
# definida como actualizar_grafo_residual(grafo_residual, u, v, valor), que recibe el grafo residual,
# una arista dirigida dada por los vértices u y v, y el nuevo valor del flujo a través de la arista (u,v)
# y actualiza el grafo residual ya teniendo en cuenta el peso anterior de la arista, y su antiparalela.
# Devolver un diccionario con los valores de los flujos para todas las aristas del grafo original.

from collections import deque

from grafo import Grafo


# asumiendo que ya viene un grafo dirigido
def ford_fulkerson(grafo: Grafo, fuente, sumidero) -> dict:
    grafo_residual = Grafo(es_dirigido=True, vertices_init=grafo.obtener_vertices())
    flujo = {}
    for v in grafo:
        for w in grafo.adyacentes(v):
            grafo_residual.agregar_arista(v, w, grafo.peso_arista(v, w))
            flujo[(v, w)] = 0
    camino = obtener_camino(grafo_residual, fuente, sumidero)
    while camino is not None:
        capacidad_residual = obtener_arista_minima(grafo_residual, camino)
        for i in range(1, len(camino)):
            v, w = camino[i - 1], camino[i]
            if grafo.estan_unidos(v, w):
                flujo[(v, w)] += capacidad_residual
            else:
                flujo[(w, v)] -= capacidad_residual
            actualizar_grafo_residual(grafo_residual, v, w, capacidad_residual)
        camino = obtener_camino(grafo_residual, fuente, sumidero)
    return flujo


def obtener_arista_minima(grafo_residual: Grafo, camino: list) -> int | float:
    minimo = float("inf")
    for i in range(1, len(camino)):
        v, w = camino[i - 1], camino[i]
        if grafo_residual.peso_arista(v, w) < minimo:
            minimo = grafo_residual.peso_arista(v, w)
    return minimo


def obtener_camino(grafo_residual: Grafo, fuente, sumidero) -> list | None:
    padres = bfs(grafo_residual, fuente, sumidero)
    camino = []
    actual = sumidero
    while actual is not None:
        camino.append(actual)
        actual = padres[actual]
    return None if len(camino) == 0 else camino[::-1]


def bfs(grafo: Grafo, origen, destino) -> dict:
    padres = {origen: None}
    visitados = set(origen)
    cola = deque()
    cola.append(origen)
    while cola:
        v = cola.popleft()
        if v == destino:
            break
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                cola.append(w)
                padres[w] = v
    return padres

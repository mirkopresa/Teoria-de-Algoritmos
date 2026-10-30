# Dada una red residual, dar un algoritmo que encuentre un camino de aumento que minimice el número de aristas utilizadas.

from collections import deque

from grafo import Grafo


def obtener_camino_de_aumento(red_residual: Grafo, s, t) -> list:
    visitados = set()
    visitados.add(s)
    padres = {s: None}
    cola = deque()
    cola.append(s)
    while cola:
        v = cola.popleft()
        if v == t:
            break
        for w in red_residual.adyacentes(v):
            if w not in visitados:
                cola.append(w)
                padres[w] = v
                visitados.add(w)
    return reconstruir_camino(padres, t)


def reconstruir_camino(padres: dict, destino) -> list:
    if destino not in padres:
        return []
    actual = destino
    camino = []
    while actual is not None:
        camino.append(actual)
        actual = padres[actual]
    return camino[::-1]

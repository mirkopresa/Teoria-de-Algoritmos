from collections import deque


def es_bipartito(grafo) -> bool:
    orden = {}
    visitados = set()
    for v in grafo:
        if v not in visitados:
            bipartito = bipartito_bfs(grafo, v, orden, visitados)
            if not bipartito:
                return False
    return True


def bipartito_bfs(grafo, inicio, orden: dict, visitados: set) -> bool:
    orden[inicio] = 0
    visitados.add(inicio)
    cola = deque()
    cola.append(inicio)
    while cola:
        v = cola.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                orden[w] = orden[v] + 1
                visitados.add(w)
                cola.append(w)
            elif orden[v] == orden[w]:
                return False
    return True

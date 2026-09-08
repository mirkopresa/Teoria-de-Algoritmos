# Un camino hamiltoniano, es un camino de un grafo, que visita todos los vértices del grafo una sola vez.
# Implementar un algoritmo por backtracking que encuentre un camino hamiltoniano de un grafo dado.


def camino_hamiltoniano(grafo) -> list:
    for v in grafo:
        solucion = hamiltoniano_rec(grafo, v, [], set())
        if solucion is not None:
            return solucion
    return []


def hamiltoniano_rec(grafo, v_actual, camino: list, visitados: set) -> list | None:
    visitados.add(v_actual)
    camino.append(v_actual)
    if len(visitados) == len(grafo):
        return camino
    for w in grafo.adyacentes(v_actual):
        if w not in visitados:
            res = hamiltoniano_rec(grafo, w, camino, visitados)
            if res is not None:
                return res
    visitados.remove(v_actual)
    camino.pop()
    return None

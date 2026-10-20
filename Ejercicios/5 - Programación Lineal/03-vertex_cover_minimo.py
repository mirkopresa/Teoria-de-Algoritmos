# Implementar un modelo de programación lineal que resuelva el problema de Vertex Cover mínimo (ejercicio 13 de BT).

import pulp


def vertex_cover_min(grafo) -> list:
    problem = pulp.LpProblem("Vertex Cover minimo", pulp.LpMinimize)
    entran = {}
    for v in grafo:
        entran[v] = pulp.LpVariable(f"V{v}", cat=pulp.LpBinary)
    visitados = set()
    for v in grafo:
        for w in grafo.adyacentes(v):
            if w not in visitados:
                problem += entran[v] + entran[w] >= 1
        visitados.add(v)
    problem += pulp.lpSum(entran[v] for v in grafo)
    problem.solve()
    resultado = []
    for v, valor in entran.items():
        if pulp.value(valor) == 1.0:
            resultado.append(v)
    return resultado

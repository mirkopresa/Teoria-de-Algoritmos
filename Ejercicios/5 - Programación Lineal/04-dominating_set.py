# Implementar un modelo de programación lineal que resuelva el problema de Dominating Set mínimo (ejercicio 14 de BT).

import pulp


def dominating_set(grafo) -> list:
    problem = pulp.LpProblem("Dominating Set minimo", pulp.LpMinimize)
    entran = {}
    for v in grafo:
        entran[v] = pulp.LpVariable(f"V{v}", cat=pulp.LpBinary)
    for v in grafo:
        problem += entran[v] + pulp.lpSum(entran[w] for w in grafo.adyacentes(v)) >= 1
    problem += pulp.lpSum(entran[v] for v in grafo)
    problem.solve()
    resultado = []
    for v, valor in entran.items():
        if pulp.value(valor) == 1.0:
            resultado.append(v)
    return resultado

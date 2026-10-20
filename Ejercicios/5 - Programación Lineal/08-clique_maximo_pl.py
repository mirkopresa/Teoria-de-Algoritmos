# Implementar un modelo de programación lineal que permita determinar el clique de tamaño máximo dentro de un grafo.
# Indicar la cantidad de restricciones generadas en función de la cantidad de vértices y aristas


import pulp


def clique_maximo(grafo) -> list:
    problem = pulp.LpProblem("Clique Maximo", pulp.LpMaximize)
    entran = {}
    for v in grafo:
        entran[v] = pulp.LpVariable(f"V{v}", cat=pulp.LpBinary)
    visitados = set()
    # Por cada par de vertices no adyacentes entre si, agregamos la restriccion
    # Esta restriccion va a maximizar la cantidad de vertices adyacentes todos entre si,
    # porque solo 1 de los 2 puede estar encendido, o los 2 apagados
    # Se generan O(V^2) restricciones en el peor de los casos (todos vertices sin aristas)
    for v in grafo:
        adyacentes = set(grafo.adyacentes(v))
        for w in grafo:
            if v != w and w not in adyacentes and w not in visitados:
                problem += entran[v] + entran[w] <= 1
        visitados.add(v)
    problem += pulp.lpSum(entran[v] for v in grafo)
    problem.solve()
    resultado = []
    for v, valor in entran.items():
        if pulp.value(valor) == 1.0:
            resultado.append(v)
    return resultado

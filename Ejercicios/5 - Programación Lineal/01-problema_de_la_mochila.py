# Implementar un modelo de programación lineal que resuelva el Problema de la Mochila de valor máximo (ejercicio 7 de PD).

import pulp


def problema_de_la_mochila(elementos: list[float], pesos: list[int], capacidad_max: int) -> list[float]:
    resultado = []
    problem = pulp.LpProblem("elementos", pulp.LpMaximize)
    e = [problem.add_variable(f"e{i}", cat=pulp.LpBinary) for i in range(len(elementos))]  # entran, o no entran
    problem += pulp.lpSum(e[i] * pesos[i] for i in range(len(elementos))) <= capacidad_max
    problem += pulp.lpSum(e[i] * elementos[i] for i in range(len(elementos)))
    problem.solve()
    for i in range(len(elementos)):
        if pulp.value(e[i]) == 1.0:
            resultado.append(elementos[i])
    return resultado


print(problema_de_la_mochila([20.40, 10, 1, 50], [4, 10, 9, 6], 10))

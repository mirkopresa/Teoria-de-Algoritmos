import pulp


def juan_el_vago(trabajos: list[int]) -> list[int]:
    if len(trabajos) == 0:
        return []
    if len(trabajos) == 1:
        return [0]
    resultado = []
    cant = len(trabajos)
    problem = pulp.LpProblem("juan el vago", pulp.LpMaximize)
    trabaje = [problem.add_variable(f"T{i}", cat=pulp.LpBinary) for i in range(cant)]
    # Para todos los dias i < len(trabajos) - 1, trabaje hoy y mañana tiene que dar <= 1
    for i in range(cant - 1):
        problem += trabaje[i] + trabaje[i + 1] <= 1
    # Para el ultimo dia, trabaje hoy y ayer tiene que dar <= 1
    problem += trabaje[cant - 1] + trabaje[cant - 2] <= 1
    problem += pulp.lpSum(trabajos[i] * trabaje[i] for i in range(cant))
    problem.solve()
    for i in range(len(trabaje)):
        if pulp.value(trabaje[i]) == 1.0:
            resultado.append(i)
    return resultado


print(juan_el_vago([100, 200]))

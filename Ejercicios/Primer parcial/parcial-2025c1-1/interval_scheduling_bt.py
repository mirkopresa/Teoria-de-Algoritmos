# Recordamos el problema de Interval Scheduling: Dado un conjunto de charlas a dar, con un horario de inicio y fin cada una, determinar
# la máxima cantidad de charlas a dar de tal forma que no haya solapamiento de horarios entre ninguna de las elegidas (devolviendo
# las charlas que logran esto). Resolver el problema de Interval Scheduling utilizando backtracking.


def interval_scheduling(charlas: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return scheduling_bt(charlas, 0, ([], 0), ([], 0))


def scheduling_bt(charlas: list[tuple[int, int]], indice: int, sol_actual: tuple[list[tuple[int, int]], int], sol_optima: tuple[list[tuple[int, int]], int]) -> list[tuple[int, int]]:
    _, cantidad_opt = sol_optima
    resultado_act, cantidad_act = sol_actual
    if cantidad_act > cantidad_opt:
        sol_optima = (resultado_act[:], cantidad_act)
    if indice == len(charlas):
        return sol_optima[0]

    if es_compatible(charlas[indice], resultado_act):
        resultado_act.append(charlas[indice])
        cantidad_act += 1
        posible_optimo = scheduling_bt(charlas, indice + 1, (resultado_act, cantidad_act), sol_optima)
        if len(posible_optimo) > sol_optima[1]:
            sol_optima = (posible_optimo[:], len(posible_optimo))
        resultado_act.pop()
        cantidad_act -= 1
    return scheduling_bt(charlas, indice + 1, (resultado_act, cantidad_act), sol_optima)


def es_compatible(charla: tuple[int, int], res: list[tuple[int, int]]) -> bool:
    for i in range(len(res)):
        if charla[0] < res[i][1]:
            return False
    return True

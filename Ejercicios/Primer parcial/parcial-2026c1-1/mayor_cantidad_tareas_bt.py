# Implementar un algoritmo que, por backtracking, resuelva el problema del ejercicio 2.


def mayor_cantidad_tareas_bt(tareas: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return tareas_bt(tareas, 0, [], [])


def tareas_bt(tareas: list[tuple[int, int]], indice: int, solucion_parcial: list[tuple[int, int]], solucion_optima: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if len(solucion_parcial) > len(solucion_optima):
        solucion_optima = solucion_parcial[:]
    if indice == len(tareas):
        return solucion_optima
    if len(tareas) - indice + len(solucion_parcial) < len(solucion_optima):
        return solucion_optima
    nueva_tarea = tareas[indice]
    if es_compatible(nueva_tarea, solucion_parcial):
        solucion_parcial.append(nueva_tarea)
        solucion_optima = tareas_bt(tareas, indice + 1, solucion_parcial, solucion_optima)
        solucion_parcial.pop()
    return tareas_bt(tareas, indice + 1, solucion_parcial, solucion_optima)


def es_compatible(nueva_tarea: tuple[int, int], solucion_parcial: list[tuple[int, int]]) -> bool:
    for tarea in solucion_parcial:
        if tarea[0] > tarea[1]:
            if nueva_tarea[0] > nueva_tarea[1]:
                return False
            if tarea[0] < nueva_tarea[1]:
                return False
            if tarea[1] > nueva_tarea[0]:
                return False
        else:
            if nueva_tarea[0] > nueva_tarea[1]:
                if tarea[0] < nueva_tarea[1]:
                    return False
                if tarea[1] > nueva_tarea[0]:
                    return False
            if nueva_tarea[0] < tarea[1]:
                return False
    return True

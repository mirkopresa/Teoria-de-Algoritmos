# Un PathSelection de un grafo dirigido G y un conjunto de caminos P1, P2, ..., Pc, es un subconjunto de dichos caminos tal que
# ninguno de ellos compartan ningún nodo entre sí. Implementar un algoritmo que dado obtenga el PathSelection más grande
# posible de un Grafo y un conjunto de caminos dado. Obviamente, implementarlo con un algoritmo por backtracking


def path_selection(caminos: list[list]) -> list:
    res, _ = path_bt(caminos, 0, ([], set()))
    return res


def path_bt(caminos: list[list], indice_caminos: int, sol_actual: tuple[list, set]) -> tuple[list, set]:
    res_actual, v_actuales = sol_actual
    if indice_caminos == len(caminos):
        return (res_actual[:], v_actuales.copy())
    res1 = ([], set())
    if es_compatible(sol_actual, caminos[indice_caminos]):
        res_actual.append(caminos[indice_caminos])
        # Agrego cada vertice del nuevo camino al set
        for v in caminos[indice_caminos]:
            v_actuales.add(v)
        res1 = path_bt(caminos, indice_caminos + 1, (res_actual, v_actuales))
        res_actual.pop()
        # Saco todos los vertices del camino del set
        for v in caminos[indice_caminos]:
            v_actuales.remove(v)
    res2 = path_bt(caminos, indice_caminos + 1, (res_actual, v_actuales))
    return res1 if len(res1[0]) > len(res2[0]) else res2


def es_compatible(solucion_actual: tuple[list, set], nuevo_camino: list) -> bool:
    if len(solucion_actual[1]) == 0:
        return True
    for v in nuevo_camino:
        if v in solucion_actual[1]:
            return False
    return True


print(path_selection([[1, 2, 3], [10, 4, 20], [4, 5, 6]]))

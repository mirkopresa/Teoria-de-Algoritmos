# Ejercicio extra
# Dados n elementos de diferentes pesos p_i, se quiere ubicar a cada elemento en algun contenedor, donde cada contenedor contiene
# capacidad maxima M (todos los contenedores tienen la misma capacidad). Suponer que todos los p_i son menores o iguales a M.
# Implementar un algoritmo de backtracking que permita minimizar la cantidad de contenedores


def bin_packing(elementos: list[int], capacidad_contenedor: int) -> list[list[int]]:
    solucion_optima = [([], 0) for _ in range(len(elementos))]
    res = bin_packing_bt(elementos, 0, capacidad_contenedor, [], solucion_optima)
    return [lista[0] for lista in res]


def bin_packing_bt(elementos: list[int], indice: int, capacidad_contenedor: int, solucion_parcial: list, solucion_optima: list) -> list:
    if len(solucion_parcial) >= len(solucion_optima):
        return solucion_optima
    if indice == len(elementos):
        if len(solucion_parcial) < len(solucion_optima):
            solucion_optima = [[res_parcial[0][:], res_parcial[1]] for res_parcial in solucion_parcial]
        return solucion_optima
    elem_actual = elementos[indice]
    for i in range(len(solucion_parcial)):
        _, capacidad = solucion_parcial[i]
        if elem_actual + capacidad <= capacidad_contenedor:
            solucion_parcial[i][0].append(elem_actual)
            solucion_parcial[i][1] += elem_actual
            solucion_optima = bin_packing_bt(elementos, indice + 1, capacidad_contenedor, solucion_parcial, solucion_optima)
            solucion_parcial[i][0].pop()
            solucion_parcial[i][1] -= elem_actual
    solucion_parcial.append([[elem_actual], elem_actual])
    solucion_optima = bin_packing_bt(elementos, indice + 1, capacidad_contenedor, solucion_parcial, solucion_optima)
    solucion_parcial.pop()
    return solucion_optima

# Implementar un algoritmo greedy que dada una lista de intervalos de formato [a, b] (con a <= b) determine el menor conjunto
# de intervalos que incluyan el mismo rango que los intervalos originales. Indicar y justificar la complejidad del algoritmo. Justificar
# por qué es un algoritmo Greedy. ¿El algoritmo da siempre la solución óptima? Si lo hace, justificar, si no dar un contraejemplo.
# Ejemplos:
# [1, 3], [5, 7], [2, 4] → [1, 4], [5, 7]
# [3, 5], [1, 2], [2, 3], [7, 10], [5, 7] → [1, 10]
# [5, 8], [3, 7], [4, 5], [10, 15], [9, 13], [11, 14] → [3, 8], [9, 15]
# [1.3, 2.8], [2.97, 3.2], [0, 1.5], [2.95, 3] → [0, 2.8], [2.95, 3.2]
# Notar que, por ejemplo, para el primer ejemplo no sería válido definir el intervalo [1, 7] porque incluiría el rango [4, 5] el cual no
# se encuentra incluído entre los originales.

# Regla greedy: ordenar de menor a mayor los intervalos por inicio, e ir extendiendo el rango del intervalo actual
# Si no cumple que se puedan conectar, guardamos el intervalo actual y el intervalo que no pudo conectar es el nuevo actual

# Optimo local: El intervalo que me maximiza la posibilidad de extender mi intervalo actual

# Optimo global: Minimizar la cantidad de intervalos

# Es optimo? Si, ya que tratamos de cubrir la mayor cantidad de rango mientras se puedan conectar, y al momento de no poderlo hacer,
# creamos uno nuevo y repetimos el progreso. Los intervalos que ya estan cubiertos no son considerados

# O(n log n), siendo n la cantidad de intervalos, debido a que ordenamos el arreglo y lo iteramos n-1 veces realizando operaciones O(1)
def menor_conjunto_intervalos(intervalos: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if len(intervalos) == 0:
        return []
    ordenados = sorted(intervalos)  # ordenamos de menor a mayor por inicio
    intervalo_actual = ordenados[0]
    res = []
    for i in range(1, len(ordenados)):
        inicio, fin = ordenados[i]
        if inicio <= intervalo_actual[1]:
            if intervalo_actual[0] <= inicio and intervalo_actual[1] >= fin:
                continue
            intervalo_actual = (intervalo_actual[0], fin)
        else:
            res.append(intervalo_actual)
            intervalo_actual = (inicio, fin)
    res.append(intervalo_actual)
    return res

# Analicemos la siguiente variante del problema de scheduling que vimos en clase. Tenemos un procesador que puede operar 24 horas
# al día, todos los días. Tenemos diferentes tareas, donde cada una tiene un horario de inicio y fin fijos. Si se decide realizar una
# determinada tarea, esta se realiza todos los días. Considerar que algunos trabajos pueden empezar antes de la medianoche y terminar
# luego de medianoche, y he aquí la diferencia con el problema de scheduling que vimos en clase.
# Dada una lista de n tareas, implementar un algoritmo greedy que nos devuelva el listado de mayor cantidad de tareas que se
# puedan realizar, considerando que el procesador solo puede ejecutar una tarea en un determinado momento. Indicar y justificar
# la complejidad del algoritmo. Justificar por qué es un algoritmo Greedy. ¿El algoritmo da siempre la solución óptima? Si lo hace,
# justificar, si no dar un contraejemplo.
# Por ejemplo, si tenemos las tareas definidas por los siguientes intervalos:
# (6 P.M., 6 A.M.), (9 P.M., 4 A.M.), (3 A.M., 2 P.M.), (1 P.M., 7 P.M.)
# La solución óptima sería elegir el trabajo de (9 P.M., 4 A.M.) y el de (1 P.M., 7 P.M.)

# Regla greedy: separar las tareas de dia con las que cruzan las de media noche, y ordenar por fin las tareas de dia
# Luego obtener la mejor solucion posible para las tareas de dia, insertando las que terminen antes mientras no hayan intersecciones
# Por ultimo, forzamos una tarea de media noche y volvemos a intentar obtener la mejor solucion con las tareas de dia
# Si es mejor que la solucion obtenida anteriormente, actualizamos

# Optimo local: la tarea que me minimiza el tiempo cubierto (y maximiza el tiempo restante)

# Optimo global: maximizar la cantidad de tareas hechas

# Es optimo? Si, debido a que primero resolvemos las tareas de dia, que es un problema ya visto en clase y que era optimo,
# y luego debido a que solo podemos tener una tarea de media noche, forzamos a tener una sola de media noche para volver a probar
# con el mismo algoritmo las tareas de dia. Si ahora que tenemos una de la noche,
# es mejor que la anterior solucion (es decir, la mejor solucion forzando 1 tarea que cruza la noche
# + las tareas de dia que no intersequen no interseco con la mejor solucion de dia), se mejora la solucion

# Complejidad: O(n²)
# Por que?
# Primero comenzamos distribuyendo las tareas: O(n)
# Luego ordenamos las tareas de dia (suponiendo que todas eran de dia, O(n log n) e insertamos cada una en la solucion mientras no haya interseccion O(n)
# Luego, en el caso de que no hayan tareas cruzadas, la complejidad es O(n log n)
# Pero en el caso de que hayan tareas cruzadas, la complejidad pasa a ser O(k * (n - k))
# Si k == n, es decir, todas las tareas son nocturnas, el algoritmo es O(n)
# Si k < n , ejemplo k = n/2 (maximo valor), O(n/2 * (n - n/2))  -> O(n²/4)
# Por ende, el algoritmo en el peor de los casos es O(n²)
def mayor_cantidad_tareas(tareas: list[tuple[int, int]]) -> list[tuple[int, int]]:
    mejor_solucion = []
    tareas_de_dia, tareas_cruzadas = obtener_tareas(tareas)
    ordenadas = sorted(tareas_de_dia, key=lambda x: x[1])
    for tarea_de_dia in ordenadas:
        if len(mejor_solucion) == 0 or not interseccion(tarea_de_dia, mejor_solucion[-1]):
            mejor_solucion.append(tarea_de_dia)
    for tarea_cruzada in tareas_cruzadas:
        sol_actual = [tarea_cruzada]
        for tarea_de_dia in ordenadas:
            if interseccion_nocturna(tarea_de_dia, sol_actual[0]):
                continue
            if len(sol_actual) == 1 or not interseccion(tarea_de_dia, sol_actual[-1]):
                sol_actual.append(tarea_de_dia)
        if len(sol_actual) > len(mejor_solucion):
            mejor_solucion = sol_actual
    return mejor_solucion


def obtener_tareas(tareas: list[tuple[int, int]]) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    resultado_1, resultado_2 = [], []
    for tarea in tareas:
        if tarea[0] < tarea[1]:
            resultado_1.append(tarea)
        else:
            resultado_2.append(tarea)
    return resultado_1, resultado_2


def interseccion(tarea_nueva: tuple[int, int], ultima: tuple[int, int]) -> bool:
    return ultima[1] > tarea_nueva[0]


def interseccion_nocturna(tarea_nueva: tuple[int, int], ultima: tuple[int, int]) -> bool:
    return ultima[0] < tarea_nueva[1] or ultima[1] > tarea_nueva[0]


print(mayor_cantidad_tareas([(18, 6), (21, 4), (3, 14), (13, 19)]))

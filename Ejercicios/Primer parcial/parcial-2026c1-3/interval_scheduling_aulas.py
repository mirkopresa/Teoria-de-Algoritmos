# Planteamos otra variante del problema de interval scheduling. Tenemos una secuencia de charlas a dar con horario de inicio y fin
# (fin > inicio). En este caso, queremos dar todas las charlas, por lo que necesitaremos más de un auditorio/aula para darlas, y que
# no hayan solapamientos. Nos interesa minimizar cantidad de aulas que necesitamos para dar todas las charlas, de tal forma que en
# una misma aula no hayan dos charlas que se solapen entre sí. Implementar un algoritmo que devuelva la conformación de estas aulas.
# Este problema puede resolverse de forma óptima, y se espera que así se resuelva. ¿El algoritmo da siempre la solución óptima? Si lo
# hace, justificar. Si no lo es, dar un contraejemplo. Justificar por qué es un algoritmo Greedy. Indicar y justificar la complejidad.

# Regla greedy: ordenar de menor a mayor las charlas por inicio, e ir insertando las charlas en un aula mientras no haya interseccion
# Si en todas las aulas la nueva charla interseca, se crea una nueva aula con esta charla

# Optimo local: la charla que me minimiza los huecos

# Optimo global: minimizar la cantidad de aulas usadas

# Es optimo? Si, porque al ordenar por inicio, nos aseguramos de conectar las charlas de cada aula entre si dejando minimos huecos posibles
# mientras que ordenando por fin, tendriamos casos en los que dejariamos huecos que nos obligarian en el futuro a crear un nuevo aula
# cuando podriamos haber organizado las charlas de manera diferente

# Complejidad: O(n^2), siendo n la cantidad de charlas
# Por que? En el peor de los casos, todas las charlas se intersecan entre si
# Por lo que por cada charla, vamos a revisar todas las aulas, ver que interseca, agregar un nuevo aula
# En una iteracion i, revisaremos i-1 aulas, por lo que O(n(n-1)) = O(n^2)
def min_aulas_interval_scheduling(charlas: list[tuple[int, int]]) -> list[list[tuple[int, int]]]:
    if len(charlas) == 0:
        return []
    resultado = [[]]
    ordenadas = sorted(charlas)  # ordenar por inicio
    for charla in ordenadas:
        interseccion = True
        for aula in resultado:
            if len(aula) == 0 or not hay_interseccion(charla, aula[-1]):
                aula.append(charla)
                interseccion = False
                break
        if interseccion:
            resultado.append([charla])
    return resultado


def hay_interseccion(charla_a_dar: tuple[int, int], charla_dada: tuple[int, int]) -> bool:
    return charla_a_dar[0] < charla_dada[1]

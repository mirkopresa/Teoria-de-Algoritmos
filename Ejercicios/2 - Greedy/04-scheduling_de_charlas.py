# Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin.
# Implementar un algoritmo Greedy que reciba el arreglo de los horarios de las charlas, representando en tuplas
# los horarios de inicios de las charlas, y sus horarios de fin, e indique cuáles son las charlas a dar para maximizar la cantidad total de charlas.
# Indicar y justificar la complejidad del algoritmo implementado.


# Complejidad: O(n log n)

# Regla greedy: ordenar los horarios de memor a mayor por fin, y obtener el que termine lo antes posible
# sin que haya intersecciones

# Optimo local: la charla actual que yo quiero dar

# Optimo global: maximizar la cantidad de charlas dadas


def charlas(horarios: list[tuple[int, int]]) -> list[tuple[int, int]]:
    resultado = []
    # ordenadas de menor a mayor por fin (O(n log n))
    ordenado = sorted(horarios)
    for charla in ordenado:  # O(n)
        if len(resultado) == 0 or not interseccion(resultado[-1], charla):  # O(1)
            resultado.append(charla)
    return resultado


# Si el inicio de una charla que quiero dar, es mayor al final de la que ya di, entonces se intersectan
def interseccion(charla_dada: tuple[int, int], charla_a_dar: tuple[int, int]) -> bool:
    return charla_a_dar[0] < charla_dada[1]

# Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin.
# Implementar un algoritmo Greedy que reciba el arreglo de los horarios de las charlas, representando en tuplas
# los horarios de inicios de las charlas, y sus horarios de fin, e indique cuáles son las charlas a dar para maximizar la cantidad total de charlas.
# Indicar y justificar la complejidad del algoritmo implementado.


# Complejidad: O(n log n)
# Regla basica: Ordenando los horarios y recorriendolos, agarramos la charla que termine lo mas antes posible,
# y esta no se tiene que intersectar con la ultima que ya di (en el caso de haber dado una ya)
# Esta nos permite encontrar un optimo local, y repitiendola varias veces, llegamos a un optimo global
# Es un algoritmo greedy al utilizar esta regla, nos fijamos en el estado actual y siguiendo esta regla
# tomamos una decision una y otra vez
def charlas(horarios: list[tuple[int, int]]) -> list[tuple[int, int]]:
    resultado = []
    ordenado = ordenar_charlas(
        horarios
    )  # ordenadas de menor a mayor por fin (O(n log n))
    for charla in ordenado:  # O(n)
        if len(resultado) == 0 or not interseccion(resultado[-1], charla):  # O(1)
            resultado.append(charla)
    return resultado


# Si el inicio de una charla que quiero dar, es mayor al final de la que ya di, entonces se intersectan
def interseccion(charla_dada: tuple[int, int], charla_a_dar: tuple[int, int]) -> bool:
    return charla_a_dar[0] < charla_dada[1]


def ordenar_charlas(horarios: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if len(horarios) <= 1:
        return horarios
    mitad = len(horarios) // 2
    mitad_izq = ordenar_charlas(horarios[:mitad])
    mitad_der = ordenar_charlas(horarios[mitad:])
    return merge(mitad_izq, mitad_der)


def merge(
    mitad_izq: list[tuple[int, int]], mitad_der: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    resultado = []
    i, j = 0, 0
    while i < len(mitad_izq) and j < len(mitad_der):
        if mitad_izq[i][1] >= mitad_der[j][1]:
            resultado.append(mitad_der[j])
            j += 1
        else:
            resultado.append(mitad_izq[i])
            i += 1
    resultado.extend(mitad_izq[i:])
    resultado.extend(mitad_der[j:])
    return resultado

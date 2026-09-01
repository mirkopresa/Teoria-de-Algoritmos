# Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total.
# Queremos maximizar el valor de lo que llevamos sin exceder la capacidad.
# Implementar un algoritmo Greedy que, reciba dos arreglos de valores y pesos de los elementos,
# y devuelva qué elementos deben ser guardados para maximizar la ganancia total.
# Indicar y justificar la complejidad del algoritmo implementado.
# ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar.
# ¿Por qué se trata de un algoritmo Greedy? Justificar


import heapq

# Regla greedy: obtener el elemento que maximice el valor/peso

# Optimo local: elegir el elemento con el ratio mas alto sin superar la capacidad de la mochila

# No, no encuentra la solucion optima siempre
# Contraejemplo:
# Mochila con capacidad 10, y tenemos elementos [(3, 1), (10, 10)]
# Relacion peso de cada una: [3, 1]
# Al ordenar de mayor a menor, o desencolar de un heap, guardaremos el elemento que tiene
# (3, 1) con relacion de peso 3, y ya no nos quedara espacio para el elemento de (10, 10)
# que era el que maximizaba el valor de los elementos


# Cada elemento i de la forma (valor, peso)
# Complejidad: O(n log n), siendo n la cantidad de elementos a evaluar
def mochila(elementos: list[tuple[int, int]], W: int) -> list[tuple[int, int]]:
    resultado = []
    peso_actual = 0
    promedios = obtener_promedios(elementos)
    heapq.heapify(promedios)  # O(n)
    while len(promedios) > 0:  # O(n log n) desencolar en un heap n veces
        _, elemento = heapq.heappop(promedios)
        if peso_actual + elemento[1] <= W:
            resultado.append(elemento)
            peso_actual += elemento[1]
    return resultado


def obtener_promedios(
    elementos: list[tuple[int, int]],
) -> list[tuple[float, tuple[int, int]]]:
    promedios = []
    for valor, peso in elementos:
        promedios.append((-(valor / peso), (valor, peso)))
    return promedios

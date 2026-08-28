# Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total.
# Queremos maximizar el valor de lo que llevamos sin exceder la capacidad.
# Implementar un algoritmo Greedy que, reciba dos arreglos de valores y pesos de los elementos,
# y devuelva qué elementos deben ser guardados para maximizar la ganancia total.
# Indicar y justificar la complejidad del algoritmo implementado.
# ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar.
# ¿Por qué se trata de un algoritmo Greedy? Justificar


import heapq

# Regla basica: obtenemos la relacion valor/peso de cada elemento, y lo ordenamos/encolamos en un heap
# Esto nos permite guardar los mejores elementos en base a la relacion valor/peso (optimo local), fijandonos en cada
# paso el estado actual de la mochila, es decir, que no este llena
# Repetimos varias veces hasta llenar la mochila o recorrer todos los elementos para llegar a un optimo global

# Va a encontrar la solucion optima siempre y cuando los valores sean positivos > 0
# Si no, ejemplo de valores menores o iguales a 0, tenemos elementos que nos van a sumar peso y nos van a restar valor,
# mientras la mochila tenga espacio, ya que estos elementos estaran al final, y
# el algoritmo los podria agarrar y guardar como resultado, restandonos valor
# Tambien, los pesos tienen que ser < a 0, porque sino tendriamos un problema al calcular el promedio en el caso de que el peso sea 0
# y en el caso de que no, al estar ordenado de mayor a menor, estos elementos que nos restan peso de la mochila y nos dan valor, nos
# quedan al final y pueden no ser incluidos


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

# Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco.
# Decidió en este caso robar toda una calle en un barrio privado, que tiene la particularidad de ser circular.
# Gracias a los trabajos de inteligencia realizados, sabemos cuánto se puede obtener por robar en cada casa.
# Podemos enumerar a la primer casa como la casa 0, de la cual podríamos obtener g0, la casa a su derecha es la 1, que nos daría g1,
# y así hasta llegar a la casa n-1, que nos daría gn-1. Toda casa se considera adyacente a las casas i-1 e i+1.
# Además, como la calle es circular, la casas 0 y n-1 también son vecinas.
# El problema con el que cuenta el Lunático es que sabe de experiencias anteriores que, si roba en una casa,
# los vecinos directos se enterarían muy rápido. No le daría tiempo a luego intentar robarles a ellos.
# Es decir, para robar una casa debe prescindir de robarle a sus vecinos directos.
# El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible.
# Dado que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema.
# Implementar un algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles casas habría que robar,
# a partir de recibir un arreglo de las ganancias obtenibles.
# Para esto, escribir y describir la ecuación de recurrencia correspondiente.
# Indicar y justificar la complejidad del algoritmo propuesto.

# Casos bases:
# 0 casas -> []
# 1 casa -> [0]
# 2 casas -> indice de max(ganancias[0], ganancias[1])
# 3 casas -> indice del maximo entre las 3 casas

# Ecuacion de recurrencia: optimo[i] = max(optimo[i-1], ganancias[i] + optimo[i-2])

# Complejidad temporal: O(n), siendo n la cantidad de casas
def lunatico(ganancias: list[int]) -> list[int]:
    if len(ganancias) == 0:
        return []
    if len(ganancias) == 1:
        return [0]
    if len(ganancias) == 2:
        if ganancias[0] > ganancias[1]:
            return [0]
        return [1]
    if len(ganancias) == 3:
        if ganancias[0] > ganancias[1] and ganancias[0] > ganancias[2]:
            return [0]
        if ganancias[1] > ganancias[0] and ganancias[1] > ganancias[2]:
            return [1]
        return [2]

    # Robamos la primera casa (y no la ultima), y calculamos la ganancia maxima sin contar la ultima
    optimos_robar_primera = obtener_optimo(ganancias, 0)
    # No robamos la primera casa (y tenemos la ultima como posible a robar) y calculamos la ganancia maxima contando la ultima
    optimos_no_robar_primera = obtener_optimo(ganancias, 1)

    if optimos_robar_primera[-1] > optimos_no_robar_primera[-1]:
        return reconstruir(optimos_robar_primera, 0)
    return reconstruir(optimos_no_robar_primera, 1)


def obtener_optimo(ganancias: list[int], desfase: int) -> list[int]:
    optimos = [ganancias[0 + desfase], max(ganancias[0 + desfase], ganancias[1 + desfase])]
    for i in range(2, len(ganancias) - 1):
        optimos.append(max(optimos[i - 1], ganancias[i + desfase] + optimos[i - 2]))
    return optimos


def reconstruir(optimos: list[int], desfase: int) -> list[int]:
    i = len(optimos) - 1
    resultado = []
    while i >= 0:
        if i == 0:
            resultado.append(i + desfase)
            break
        if optimos[i] == optimos[i - 1]:
            i -= 1
        else:
            resultado.append(i + desfase)
            i -= 2
    return resultado[::-1]

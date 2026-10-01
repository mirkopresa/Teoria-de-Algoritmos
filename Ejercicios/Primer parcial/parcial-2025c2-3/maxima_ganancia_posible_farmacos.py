# El famoso ladrón Francesco Rizzoli (hermano del “árbitro” de la final del 2014), ha decidido hacer un atraco a un laboratorio
# farmacéutico. Allí puede robarse diferentes fármacos que se están estudiando (en formato líquido). Tiene un catálogo del valor de
# cada fármaco, que puede vender en el mercado negro. De cada fármaco hay una diferente cantidad disponible (medible en ml). Rizzoli
# sólo tiene posibilidad en su equipo de llevarse como máximo L ml en fármacos. Lo bueno es que sabe que puede fraccionar y poner
# proporciones de los fármacos; y en ese caso lo vendería en su valor proporcional. Implementar un algoritmo greedy que obtenga los
# fármacos (y cantidades) que Rizzoli debe robarse para obtener la máxima ganancia posible (el algoritmo debe ser óptimo, en esta
# familia no se aceptan los robos a medias). Justificar por qué el algoritmo propuesto es Greedy y por qué es, en efecto, óptimo. Indicar
# y justificar la complejidad del algoritmo implementado.

# Regla greedy: Ordenar los farmacos de mayor a menor por coeficiente valor/peso, e ir insertando cada uno, hasta que la mochila se llene
# actualizando la capacidad actual de la mochila. Una vez que el proximo elemento vaya a sobrepasar la capacidad de la mochila, fraccionamos el elemento
# y lo metemos

# Optimo local: el elemento actual que me maximiza el valor minimizando el peso ocupado

# Optimo global: maximizar el valor total

# Es optimo? Si, debido a que nos aseguramos de insertar los elementos que mejor cumplan la relacion valor/peso y al momento de que ya no podemos insertar
# mas elementos porque sobrepasamos el peso, fraccionamos el proximo para asi no perdernos ese valor extra

# O(n log n), debido a que ordenamos el arreglo de farmacos de mayor a menor por coeficiente valor/peso
# Luego hacemos un recorrido lineal y hacemos operaciones O(1)
def atraco_farmaceutico(farmacos: list[tuple[int, int]], l_maximo: int) -> list[tuple[int, int]]:
    resultado = []
    ordenados = ordenar_farmacos_promedio(farmacos)  # ordenado de mayor a menor por coeficiente valor/cantidad_ml
    for i in range(len(ordenados)):
        _, producto = ordenados[i]
        valor, capacidad_a_ocupar = producto
        if capacidad_a_ocupar <= l_maximo:
            resultado.append((valor, capacidad_a_ocupar))
            l_maximo -= capacidad_a_ocupar
        if l_maximo == 0:
            break
        if capacidad_a_ocupar > l_maximo:
            factor = l_maximo / capacidad_a_ocupar
            resultado.append((valor * factor, capacidad_a_ocupar % l_maximo))
            break
    return resultado


def ordenar_farmacos_promedio(farmacos: list[tuple[int, int]]) -> list[tuple[float, tuple[int, int]]]:
    resultado = [(farmacos[i][0] / farmacos[i][1], farmacos[i]) for i in range(len(farmacos))]
    return sorted(resultado, key=lambda x: x[0], reverse=True)

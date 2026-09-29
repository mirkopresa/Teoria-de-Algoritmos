# Laura está de viaje por Japón y entró a un Centro Pokemon, a comprar merchandising. Va a tratar de llevarse todo lo más valioso
# (para ella) que pueda y que entre en su mochila. Tiene 2 limitaciones. La primera: no puede guardar más peso que lo que permita su
# mochila (tiene límite hasta W ).
# La segunda: como sabe que puede entrar en un estado de locura e inconciencia temporal, se puso
# un límite que no comprará por más de P precio en total (es decir, la suma de todo lo comprado).
# Cada producto tiene 3 valores asociados: su valor (vi, que Laura definió en base a su subjetividad), su precio (pi) y su peso (wi).
# Implementar un algoritmo que, utilizando programación dinámica, permita determinar qué productos debe comprar Laura tal
# que no superen el peso máximo que puede llevar y el precio máximo dispuesto a pagar, y que logre maximizar el valor obtenido
# (dados por la suma de los elementos comprados). También escribir el algoritmo que permita reconstruir la solución.
# Indicar y justificar la complejidad del algoritmo implementado.

# Ecuacion de recurrencia: OPT[i, W, P] = max(OPT[i-1, W, P], valor_p_i + OPT[i-1, W - peso_p_i, P - precio_p_i])

# Complejidad: O(n*w*p) siendo n la cantidad de productos, w la capacidad de la mochila, y p el precio limite
# debido a que creamos una matriz tridimensional n*w*p y la recorremos completamente haciendo operaciones O(1)
# La reconstruccion tiene un costo de O(n) que es menor a O(n*w*p)
def merchandising_pd(productos: list[tuple[int, int, int]], precio_max: int, capacidad_max: int) -> list[tuple[int, int, int]]:
    optimos = [[[0 for _ in range(precio_max + 1)] for _ in range(capacidad_max + 1)] for _ in range(len(productos) + 1)]
    for i in range(1, len(productos) + 1):
        for j in range(1, capacidad_max + 1):
            for k in range(1, precio_max + 1):
                valor, precio, peso = productos[i - 1]
                if peso <= j and precio <= k:
                    optimos[i][j][k] = max(optimos[i - 1][j][k], valor + optimos[i - 1][j - peso][k - precio])
                else:
                    optimos[i][j][k] = optimos[i - 1][j][k]
    return reconstruir(productos, optimos, precio_max, capacidad_max)


def reconstruir(productos: list[tuple[int, int, int]], optimos: list[list[list[int]]], precio_max: int, capacidad_max: int) -> list[tuple[int, int, int]]:
    resultado = []
    i, j, k = len(productos), capacidad_max, precio_max
    while i > 0 and j >= 0 and k >= 0:
        if optimos[i][j][k] != optimos[i - 1][j][k]:
            resultado.append(productos[i - 1])
            j -= productos[i - 1][2]
            k -= productos[i - 1][1]
        i -= 1
    return resultado[::-1]

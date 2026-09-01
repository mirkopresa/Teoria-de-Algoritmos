# Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada cantidad de plata.
# Implementar un algoritmo Greedy que devuelva el cambio pedido, usando la mínima cantidad de monedas/billetes.
# El algoritmo recibirá un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar,
# y debe devolver qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizada.
# Indicar y justificar la complejidad del algoritmo implementado.
# ¿El algoritmo implementado encuentra siempre la solución óptima?
# Justificar si es óptimo, o dar un contraejemplo.
# ¿Por qué se trata de un algoritmo Greedy? Justificar


# O(n), siendo n la cantidad de monedas/billetes a devolver

# Regla greedy: Usar la moneda de mayor denominacion que no supere el monto actual

# Optimo local: La moneda que vamos a usar en el estado actual

# Optimo global: Minimizar la cantidad de monedas utilizadas

# El algoritmo siempre encuentra la solucion optima en ciertos tipos de sistemas monetarios, en otros
# no lo va a hacer, entonces es optimo para este caso, pero en general puede no serlo.

# Contraejemplo:
# Monedas: [1, 7, 8, 9] - Monto a devolver: 15
# El algoritmo nos devolveria [9, 1, 1, 1, 1, 1, 1], cuando la mejor solucion es [8, 7]


# forma entendible
def cambio(monedas: list[int], monto: int) -> list[int]:
    resultado = []
    i = len(monedas) - 1
    while i >= 0 and monto > 0:
        if monto - monedas[i] < 0:
            i -= 1
        else:
            monto -= monedas[i]
            resultado.append(monedas[i])
    return resultado


# forma pythonica
"""
def cambio(monedas: list[int], monto: int) -> list[int]:
    resultado = []
    i = len(monedas) - 1
    while i >= 0 and monto > 0:
        cantidad = monto // monedas[i]
        resto = monto % monedas[i]
        if cantidad != 0:
            monto = resto
            lista = [monedas[i]] * cantidad
            resultado += lista
        i -= 1
    return resultado
"""

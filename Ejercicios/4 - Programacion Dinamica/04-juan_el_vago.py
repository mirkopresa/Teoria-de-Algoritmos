# Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, pero no quiere trabajar dos días seguidos.
# Dado un arreglo con el monto esperado a ganar cada día, determinar, por programación dinámica, el máximo monto a ganar,
# sabiendo que no aceptará trabajar dos días seguidos. Hacer una reconstrucción para verificar qué días debe trabajar.
# Indicar y justificar la complejidad del algoritmo implementado.

# Ejemplo:
# Para: [100, 5, 50, 1, 1, 200]
# Devolver: [0, 2, 5]


# Casos base:
# suma[0] = trabajos[0]
# suma[1] = max(trabajos[0], trabajos[1])
# Ecuacion de recurrencia:
# suma[i] = max(suma[i - 1], trabajos[i] + suma[i - 2])

# Complejidad temporal: O(n) siendo n la cantidad de dias de trabajo
def juan_el_vago(trabajos: list[int]) -> list[int]:
    if len(trabajos) == 0:
        return []
    if len(trabajos) == 1:
        return [0]
    if len(trabajos) == 2:
        if trabajos[0] > trabajos[1]:
            return [0]
        return [1]
    suma = [trabajos[0], max(trabajos[0], trabajos[1])]
    for i in range(2, len(trabajos), 1):
        suma.append(max(suma[i - 1], trabajos[i] + suma[i - 2]))
    return reconstruir(suma)


def reconstruir(suma: list[int]) -> list[int]:
    i = len(suma) - 1
    res = []
    while i >= 0:
        if i == 0:
            # si estamos en el dia 0, si o si trabajamos
            res.append(i)
            break
        if suma[i] == suma[i - 1]:
            i -= 1
        else:
            res.append(i)
            i -= 2
    return res[::-1]

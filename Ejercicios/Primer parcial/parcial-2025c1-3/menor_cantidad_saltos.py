# Dado un arreglo de números positivos, donde cada elemento representa el máximo número de pasos que podemos dar desde esa
# posición, implementar un algoritmo que, utilizando programación dinámica determine la menor cantidad de saltos a realizar
# para llegar al final del arreglo (comenzamos en la posición 0). También escribir el algoritmo que permita reconstruir la solución.
# Indicar y justificar la complejidad del algoritmo implementado.
# Por ejemplo, si el arreglo es [2, 3, 1, 1, 4], la solución óptima es ir desde la posición 0 a la posición 1 (saltando 1 lugar,
# teniendo máximo 2 desde el inicio), y de allí a la posición 4 (saltando 3 lugares, que es el máximo desde dicha posición), logrando
# llegar al final en 2 saltos.

# Caso base: i = 0 -> opt[0] = 0

# Ecuacion de recurrencia: opt[i + j] = min(opt[i] + 1, opt[i + j])

# O(n²) (una verga el ej)
def menor_cantidad_saltos(arr: list[int]) -> list[int]:
    saltos = [float("inf")] * len(arr)
    saltos[0] = 0
    resultado = [0] * len(arr)
    resultado[0] = -1
    for i in range(len(arr) - 1):
        for j in range(1, arr[i] + 1):
            if i + j == len(arr):
                break
            # Basicamente, si haber saltado desde la posicion i, + 1, es menor a ya haber saltado a la posicion i + j
            if saltos[i] + 1 < saltos[i + j]:
                saltos[i + j] = saltos[i] + 1
                resultado[i + j] = i
    return reconstruir(resultado, arr)


def reconstruir(resultado: list[int], arr: list[int]) -> list[int]:
    res = []
    i = len(arr) - 1
    while i != -1:
        res.append(i)
        i = resultado[i]
    return res[::-1]


print(menor_cantidad_saltos([2, 3, 1, 1, 4]))

# Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de un número n en tiempo O(log n).
# Por ejemplo, para n = 10 debe devolver 3, y para n = 25 debe devolver 5.
# Justificar el orden del algoritmo.


def parte_entera_raiz(n: int) -> int:
    return raiz_recursivo(n, 0, n)


# A = 1, B = 2, C = 0 -> log en base 2 de 1 = 0, 0 = C, O(log n)
def raiz_recursivo(num: int, minimo: int, maximo: int) -> int:
    if minimo > maximo:
        return maximo
    mitad = (minimo + maximo) // 2
    cuadrado = mitad * mitad
    if cuadrado == num:
        return mitad
    if cuadrado < num:
        return raiz_recursivo(num, mitad + 1, maximo)
    return raiz_recursivo(num, minimo, mitad - 1)

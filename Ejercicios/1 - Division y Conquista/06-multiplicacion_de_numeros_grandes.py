# Implementar un algoritmo de multiplicación de dos números grandes de longitud n, por división y conquista,
# con un orden de complejidad mejor que O(n^2)
# Justificar la complejidad del algoritmo mediante el teorema maestro.

MIN = 50


def multiplicar(a: int, b: int) -> int:
    n = obtener_longitud(a)
    if n < MIN:
        return a * b
    a1, a0 = separar(a)
    b1, b0 = separar(b)
    p = multiplicar(a1 + a0, b1 + b0)
    a0b0 = multiplicar(a0, b0)
    a1b1 = multiplicar(a1, b1)
    return a1b1 * 10**n + (p - a0b0 - a1b1) * 10 ** (n // 2) + a0b0


def separar(n: int) -> tuple[int, int]:
    n1, n0 = n, 0
    potencia = 1
    for _ in range(obtener_longitud(n) // 2):
        n0 += (n1 % 10) * potencia
        n1 //= 10
        potencia *= 10
    return n1, n0


def obtener_longitud(n: int) -> int:
    return len(str(n))

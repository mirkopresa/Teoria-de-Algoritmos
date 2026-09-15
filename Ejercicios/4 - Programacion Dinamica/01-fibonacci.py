# Implementar un algoritmo que, utilizando programación dinámica, obtenga el valor del n-ésimo número de fibonacci.
# Indicar y justificar la complejidad del algoritmo implementado.

# Definición:

# n = 0 --> Debe devolver 1
# n = 1 --> Debe devolver 1
# n --> Debe devolver la suma entre los dos anteriores números de fibonacci (los fibonacci n-2 y n-1)


def fibonacci(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    anterior = 0
    actual = 1
    for _ in range(n):
        nuevo = actual + anterior
        anterior = actual
        actual = nuevo
    return actual

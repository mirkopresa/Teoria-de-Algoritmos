# Dada una escalera, y sabiendo que tenemos la capacidad de subir escalones de a 1 o 2 o 3 pasos, encontrar,
# utilizando programación dinámica, cuántas formas diferentes hay de subir la escalera hasta el paso n.
# Indicar y justificar la complejidad del algoritmo implementado.
# Ejemplos:

# n = 0 --> Debe devolver 1 (no moverse)
# n = 1 --> Debe devolver 1 (paso de 1)
# n = 2 --> Debe devolver 2 (dos pasos de 1, o un paso de 2)
# n = 3 --> Debe devolver 4 (un paso de 3, o tres pasos de 1, o un paso de 2 y uno de 1, o un paso de 1 y un paso de 2)
# n = 4 --> Debe devolver 7
# n = 5 --> Debe devolver 13

# Complejidad temporal: O(n)
def escalones(n: int) -> int:
    if n in {0, 1}:
        return 1
    if n == 2:
        return 2

    primero, segundo, tercero = 1, 1, 2
    for _ in range(n - 2):
        primero, segundo, tercero = segundo, tercero, primero + segundo + tercero
    return tercero

# Se sabe, por el teorema de Bolzano, que si una función es continua en un intervalo [a, b], y que en el punto a es positiva
# y en el punto b es negativa (o viceversa), necesariamente debe haber (al menos) una raíz en dicho intervalo.
# Implementar una función raiz que reciba una función (univariable) y los extremos mencionados a y b, y devuelva una raíz
# dentro de dicho intervalo (si hay más de una, simplemente quedarse con una).
# La complejidad de dicha función debe ser logarítmica del largo del intervalo [a, b].
# Asumir que por más que se esté trabajando con números enteros, hay raíz en dichos valores:
# Se puede trabajar con floats, y el algoritmo será equivalente, simplemente se plantea con ints para no generar confusiones con la complejidad.
# Justificar la complejidad de la función implementada.

# Complejidad: O(log n)
# Por que? Ecuacion de recurrencia: T(n) = T(n/2) + O(1)
# A = 1, B = 2, C = 0, log en base 2 de 1 = 0, 0 = C, O(n^c * log n) -> O(log n)
def raiz(funcion, a: int, b: int) -> int:
    funcion_a = funcion(a)
    funcion_b = funcion(b)
    if funcion_a == 0:
        return a
    if funcion_b == 0:
        return b
    mitad = (a + b) // 2
    funcion_mitad = funcion(mitad)
    if funcion_mitad == 0:
        return mitad
    if (funcion_a > 0 and funcion_mitad < 0) or (funcion_a < 0 and funcion_mitad > 0):
        return raiz(funcion, a, mitad)
    return raiz(funcion, mitad, b)

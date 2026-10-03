# Recordamos que la secuencia de Fibonacci está definida como F(0) = 0, F(1) = 1 y F(n) = F(n-1) + F(n-2) en otro caso. Ahora
# bien, existe la siguiente equivalencia (por fuera de los casos base), con k = ⌊n/2⌋ (parte entera de la mitad de n):
# F(n) = F(k) · (2F(k + 1) -  F(k)) si n es par,
# F(n) = F(k + 1)^2 + F(k)^2 si n es impar.
# Usando esto, implementar un algoritmo que, utilizando división y conquista permita obtener el n-ésimo número de la secuencia de
# Fibonacci en O(log n). Justificar adecuadamente la complejidad del algoritmo implementado.
# Ayudas:
# Considerá hacer que la función recursiva devuelva tanto F(n) como F (n + 1).
# Recordá que si n es par, entonces el valor de k es igual tanto para n como para n +1, y que si n es impar, entonces el valor de k es
# igual tanto para n como para n-1, y que la definición de la secuencia de Fibonacci sigue valiendo (F(i) = F (i-1) + F (i-2)).

# F(2) = F(1) * (2F(2) - F(1))


def n_esimo_fibonacci(n: int) -> tuple[int, int]:
    if n == 0:
        return (1, 1)
    mitad = n // 2
    # n = 3, mitad = 1, entonces esto nos da F(1), F(2)
    f_k, f_k_mas_uno = n_esimo_fibonacci(mitad)
    par, impar = f_k * (2 * f_k_mas_uno - f_k), f_k_mas_uno * f_k_mas_uno + f_k * f_k
    if n % 2 == 0:
        return (par, impar)
    # esto tiene que devolver F(2), F(3), F(3) = F(2) + F(1)
    return (impar, par + impar)

# Una función lineal se define como f(x) = a x + b.
# Si tenemos dos funciones lineales f_1(x) = a_1 x + b_1 y
# f_2(x) = a_2 x + b_2, entonces la composición puede simplificarse a:
# f_3(x) = f_1(f_2(x)) = (a_1 a_2) x + (a_1 b_2 + b_1). Es decir, tenemos una nueva función lineal, cuyos a y b son los resultates marcados.

# Utilizando división y conquista, implementar una función
# composicion_n(a, b, c, n) que reciba los valores de a y b de una función lineal,
# c y n y determine el valor de f^n(c) = f(f(f(...f(c)) (n composiciones de la
# función f consigo misma) en tiempo \mathcal{O}(\log n).
# El caso n=1 corresponderá a simplemente aplicar la función.
# Justificar adecuadamente la complejidad del algoritmo implementado.

# Recomendamos primero obtener los valores de a y b que corresponden a f^n(x). La cuenta final es trivial.

# Complejidad: O(log n)
# Por que? Ecuacion de recurrencia: T(n) = T(n/2) + O(1)
# A = 1, B = 2, C = 0, log en base 2 de 1 = 0, 0 = C, O(n^c * log n) -> O(log n)


def composicion_n(a: int, b: int, c: int, n: int) -> int:
    a_1, b_1 = composicion_n_rec(a, b, n)
    return a_1 * c + b_1


def composicion_n_rec(a: int, b: int, n: int) -> tuple[int, int]:
    if n == 1:
        return a, b
    mitad = n // 2
    a_mitad, b_mitad = composicion_n_rec(a, b, mitad)
    f_n_mitad_a, f_n_mitad_b = a_mitad * a_mitad, a_mitad * b_mitad + b_mitad
    if n % 2 == 0:
        return f_n_mitad_a, f_n_mitad_b
    return f_n_mitad_a * a, a * f_n_mitad_b + b

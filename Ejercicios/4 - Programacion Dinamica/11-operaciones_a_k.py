# Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K, siendo que las operaciones posibles son:

# (i) aumentar el valor del operando en 1;

# (ii) duplicar el valor del operando.

# Implementar un algoritmo que, por programación dinámica obtenga la menor cantidad de operaciones a realizar (y cuáles son dichas operaciones).
# Desarrollar la ecuación de recurrencia.
# Indicar y justificar la complejidad del algoritmo implementado.

# Devolver un arreglo de las operaciones a realizar en orden. En texto cada opción es 'mas1' o 'por2'

# Ecuacion de recurrencia:
# Caso par: min(operaciones_n[i - 1], operaciones_n[i // 2]) + 1
# Caso impar: operaciones_n[i - 1] + 1


def operaciones(k: int) -> list[str]:
    resultado = []
    if k == 0:
        return resultado

    operaciones_n = [0]
    # Armar el arreglo con la cantidad de operaciones por numero
    for i in range(1, k + 1):
        if i % 2 == 0:
            operaciones_n.append(min(operaciones_n[i - 1], operaciones_n[i // 2]) + 1)
        else:
            operaciones_n.append(operaciones_n[i - 1] + 1)

    # Reconstruccion
    j = k
    while j > 0:
        if operaciones_n[j - 1] + 1 == operaciones_n[j]:
            resultado.append("mas1")
            j -= 1
        else:
            resultado.append("por2")
            j //= 2
    return resultado[::-1]

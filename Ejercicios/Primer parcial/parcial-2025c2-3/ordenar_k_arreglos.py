# Implementar un algoritmo de división y conquista que reciba un arreglo de K arreglos/listas ordenadas, cada una de H elementos
# (es decir, en total hay n = K*H elementos) y devuelva un arreglo con todos los elementos, ya ordenados. El algoritmo debe utilizar la
# información del enunciado para considerarse aprobable. NO utilizar un heap para resolver el problema, se está evaluando división y
# conquista.
# Una vez implementado, puede que no sea posible utilizar el Teorema Maestro para calcular su complejidad. Explicar por qué es el caso.
# Dar cuál sería la complejidad con una breve justificación (no es necesario hacer una demostración). En caso que tu implementación sí
# permita calcular su complejidad con el Teorema Maestro, recomendamos revisar que esté bien hecho y, si lo está, dar su complejidad
# dada por el teorema.

# Complejidad: O(n*log(K)) siendo n la cantidad de elementos total del arreglo
# Por que? Hacemos una operacion O(n) log K veces, debido a que en cada iteracion de ordenar_arreglo
# partimos el problema en 2 mitades, formandose un arbol de llamadas recursivas de tamaño log K. En cada una de estas llamadas
# recursivas se realiza una operacion O(n) en total, ya que se ven todos los elementos

# El teorema maestro no se puede aplicar debido a que la ecuacion dependeria de 2 variables independientes, como la cantidad de arreglos k
# y la cantidad de elementos h
def ordenar_arreglo(arr: list[list[int]]) -> list[int]:
    if len(arr) <= 0:
        return []
    if len(arr) == 1:
        return arr[0]
    mitad = len(arr) // 2
    mitad_izq = ordenar_arreglo(arr[:mitad])
    mitad_der = ordenar_arreglo(arr[mitad:])
    return merge(mitad_izq, mitad_der)


def merge(mitad_izq: list[int], mitad_der: list[int]) -> list[int]:
    resultado = []
    i, j = 0, 0
    while i < len(mitad_izq) and j < len(mitad_der):
        if mitad_izq[i] >= mitad_der[j]:
            resultado.append(mitad_der[j])
            j += 1
        else:
            resultado.append(mitad_izq[i])
            i += 1
    resultado.extend(mitad_izq[i:])
    resultado.extend(mitad_der[j:])
    return resultado

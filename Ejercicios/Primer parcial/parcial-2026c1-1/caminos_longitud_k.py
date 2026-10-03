# Tenemos un grafo representado con una matriz de adyacencia A. Dicha matriz tiene únicamente unos y ceros (según si dos vértices
# son adyacentes, o no). Implementar un algoritmo de división y conquista que, dada la matriz A y un valor k, devuelva la cantidad
# de caminos de longitud k que hay en el grafo correspondiente. Analizar y justificar detalladamente la complejidad del algoritmo
# implementado. Tener mucho cuidado al analizar la complejidad; es probable que no puedas aplicar el teorema maestro. En dicho
# caso, como parte del análisis de la complejidad, explicar por qué no es aplicable el teorema (nuevamente, es probable que no puedas aplicarlo).
# Recomendamos recordar que:
# A^m[i][j]nos dice la cantidad de caminos de longitud m que hay entre i y j.
# Que la multiplicación de matrices se puede considerar como una operación que consume O(n ^ (log en base 2 de 7)), siendo n la dimensión de
# la matriz (cuadrada). Si bien este algoritmo es de división y conquista, no se pide ni es de interés que implementen nada al
# respecto de esto. Suponé que está disponible la función multiplicar_matrices(A, B).

# Complejidad final: O(log k * (n ^ (log en base 2 de 7))) porque log en base 2 de 7 > 2
# (tener muy en cuenta esto para el parcial)

# Complejidad: O(n^2)
def obtener_caminos_k(matriz: list[list[int]], k: int) -> int:
    matriz_k = obtener_matriz_k(matriz, k)
    contador = 0
    for i in range(len(matriz_k)):
        for j in range(len(matriz_k)):
            contador += matriz_k[i][j]
    return contador


# Complejidad: O(log k * (n ^ (log en base 2 de 7)))
# Por que? No se puede aplicar el teorema maestro porque este dependeria de 2 variables
# T(n, k) = T(n, k / 2) + O(n ^ (log en base 2 de 7))
# Entonces vamos a hacer el analisis de otra manera
# Dividimos el problema a la mitad en cada iteracion, se genera un arbol de llamadas recursivas de log k
# En cada iteracion hacemos una (o 2) operaciones (n ^ (log en base 2 de 7)
# Entonces la complejidad es O(log k * (n ^ (log en base 2 de 7))
def obtener_matriz_k(matriz: list[list[int]], k: int) -> list[list[int]]:
    if k == 1:
        return matriz
    mitad = obtener_matriz_k(matriz, k // 2)
    resultado = multiplicar_matrices(mitad, mitad)
    if k % 2 == 0:
        return resultado
    return multiplicar_matrices(resultado, matriz)

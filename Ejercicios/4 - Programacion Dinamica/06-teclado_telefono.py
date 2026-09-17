# Dado el teclado numérico de un celular, y un número inicial k, encontrar la cantidad de posibles números de longitud N empezando
# por botón del número inicial k. Restricción: solamente se puede presionar un botón si está arriba, abajo, a izquierda, o derecha del botón actual.
# Restricción: solamente se puede presionar un botón si está arriba, abajo, a izquierda, o derecha del botón actual.
# Implementar el algoritmo por programación dinámica. Indicar y justificar la complejidad del algoritmo implementado.

# Ejemplos:

# Para n=1 empezando por cualquier dígito, solamente hay un número válido (el correspondiente dígito)
# Para N=2, depende de cuál dígito se comienza.
# Empezando por 0, son válidos 08 (cantidad: 1)
# Empezando por 1, son válidos 12, 14 (cantidad: 2)
# Empezando por 2, son válidos 21, 23, 25 (cantidad: 3)
# Empezando por 3, son válidos 32, 36 (cantidad: 2)
# Empezando por 4, son válidos 41, 45, 47 (cantidad: 3)
# Empezando por 5, son válidos 52, 54, 56, 58 (cantidad: 4)
# Empezando por 6, son válidos 63, 65, 69 (cantidad: 3)
# Empezando por 7, son válidos 74, 78 (cantidad: 2)
# Empezando por 8, son válidos 80, 85, 87, 89 (cantidad: 4)
# Empezando por 9, son válidos 96, 98 (cantidad: 2)

# Caso base: n == 1 (un solo digito) -> devolvemos 1 sola posible combinacion
# Ecuacion de recurrencia: matriz_suma[num][cant_digitos] = para todo vecino: sumatoria[vecino][cant_digitos-1]

from grafo import Grafo


def numeros_posibles(k: int, n: int) -> int:
    if n == 1:
        return 1
    # Creo el grafo con forma de numeros de celular
    grafo = crear_grafo_numeros()
    # Inicializo la matriz con todos 0, de n (digitos) columnas, 10 numeros (0 al 9)
    matriz_suma = [[0] * n for _ in range(10)]
    # Le asigno el numero a la primera columna, y la cantidad de ese numero vecinos a la segunda columna (cantidad de posibles numeros de n digitos)
    for i in range(10):
        matriz_suma[i][0] = i
        matriz_suma[i][1] = len(grafo.adyacentes(i))
    # A partir de la tercera columna, por cada numero, le asignamos la sumatoria de la cantidad de numeros de n-1 digitos de cada vecino
    for i in range(2, n):
        for j in range(10):
            contador = 0
            for vecino in grafo.adyacentes(j):
                contador += matriz_suma[vecino][i - 1]
            matriz_suma[j][i] = contador
    # Devolvemos la sumatoria del numero k
    return matriz_suma[k][n - 1]


def crear_grafo_numeros() -> Grafo:
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    grafo = Grafo(es_dirigido=False, vertices_init=numeros)
    grafo.agregar_arista(numeros[0], numeros[8])

    grafo.agregar_arista(numeros[1], numeros[2])
    grafo.agregar_arista(numeros[1], numeros[4])

    grafo.agregar_arista(numeros[2], numeros[3])
    grafo.agregar_arista(numeros[2], numeros[5])

    grafo.agregar_arista(numeros[3], numeros[6])

    grafo.agregar_arista(numeros[4], numeros[5])
    grafo.agregar_arista(numeros[4], numeros[7])

    grafo.agregar_arista(numeros[5], numeros[6])
    grafo.agregar_arista(numeros[5], numeros[8])

    grafo.agregar_arista(numeros[6], numeros[9])

    grafo.agregar_arista(numeros[7], numeros[8])

    grafo.agregar_arista(numeros[8], numeros[9])
    return grafo

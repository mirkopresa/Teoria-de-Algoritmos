# Dado un laberinto representado por una grilla, queremos calcular la ganancia máxima que existe desde la posición (0,0) hasta la posición NxM.
# Los movimientos permitidos son, desde la esquina superior izquierda (el (0,0)), nos podemos mover hacia abajo o hacia la derecha.
# Pasar por un casillero determinado (i, j) nos da una ganancia de V_{i,j}.
# Implementar un algoritmo que, por programación dinámica, obtenga la máxima ganancia a través del laberinto.
# Hacer una reconstrucción del camino que se debe transitar.
# Indicar y justificar la complejidad del algoritmo implementado.
# Si hay algunos lugares por los que no podemos pasar (obstáculos), ¿cómo se debe modificar para resolver el mismo problema?

# Aclaración: solamente por simplicidad de las pruebas automáticas, devolver en este caso la ganancia máxima obtenible.
# Tener en cuenta que en un examen se pediría la reconstrucción de cómo se obtiene la ganancia.

# Casos bases:
# Si n == 0 -> 0 (matriz vacia)
# Si n == 1 -> sumatoria de las columnas
# Si m == 1 -> sumatoria de las filas
# Ecuacion de recurrencia: max(matriz_suma[i-1][j], matriz_suma[i][j-1]) + matriz[i][j]


def laberinto(matriz: list[list[int]]) -> int:
    n_filas = len(matriz)
    if n_filas == 0:
        return 0
    if n_filas == 1:
        return sum(matriz[0])
    n_columnas = len(matriz[0])
    if n_columnas == 1:
        suma = 0
        for i in range(n_filas):
            suma += matriz[i][0]
        return suma
    # Inicializacion de la matriz suma con todos 0
    matriz_suma = [[0] * n_columnas for _ in range(n_filas)]
    matriz_suma[0][0] = matriz[0][0]
    # Sumamos el actual con la suma del de arriba
    for i in range(1, n_filas):
        matriz_suma[i][0] = matriz_suma[i - 1][0] + matriz[i][0]
    # Sumamos el actual con la suma del de la izquierda
    for i in range(1, n_columnas):
        matriz_suma[0][i] = matriz_suma[0][i - 1] + matriz[0][i]
    for i in range(1, n_filas):
        # Por cada i,j sumamos el maximo entre la anterior columna y la fila de arriba, con el numero actual
        for j in range(1, n_columnas):
            matriz_suma[i][j] = max(matriz_suma[i - 1][j], matriz_suma[i][j - 1]) + matriz[i][j]
    # en caso de parcial, reconstruir
    return matriz_suma[n_filas - 1][n_columnas - 1]

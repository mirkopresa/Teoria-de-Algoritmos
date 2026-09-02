# Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se rompen.
# Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados,
# encuentre la mejor forma de distribuir los productos en la menor cantidad posible de bolsas.
# Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ].
# ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar.
# Indicar y justificar la complejidad del algoritmo implementado.

# Regla greedy: Ordenar los productos de mayor a menor, crear una bolsa con el producto actual mas grande,
# e intentar insertarle productos mas pequeños hasta que no entre nada mas

# Optimo local: La combinacion del producto mas pesado actual con los mas livianos posibles

# Optimo global: Minimizar la cantidad de bolsas usadas

# Caso en el que falla: Capacidad 10 - Productos [7, 6, 3, 2, 2]
# Va agarrar el 7, le va a meter el ultimo 2, y se va a quedar sin espacio 9/10 ya no entra nada
# Ahora agarra el 6, le mete el 2, y se queda sin espacio 8/10 ya no entra el 3
# El 3 queda en una bolsa aparte
# Resultado -> [[7, 2], [6, 2], [3]] - Resultado esperado -> [[7, 3], [6, 2, 2]]


# Complejidad O(n log n), siendo n la cantidad de productos a ordenar
def bolsas(capacidad: int, productos: list[int]) -> list[list[int]]:
    resultado = []
    capacidad_actual = 0
    ordenados = sorted(productos, reverse=True)
    inicio = 0
    fin = len(ordenados) - 1
    while inicio <= fin:
        bolsa_actual = [ordenados[inicio]]
        capacidad_actual += ordenados[inicio]
        inicio += 1
        while capacidad_actual + ordenados[fin] <= capacidad and inicio <= fin:
            bolsa_actual.append(ordenados[fin])
            capacidad_actual += ordenados[fin]
            fin -= 1
        resultado.append(bolsa_actual)
        capacidad_actual = 0
    return resultado


# Caso en el que falla el FFD: [5, 5, 4, 4, 3, 3, 3, 3] Capacidad 10
# Quedarian bolsas: [[5, 5], [4, 4], [3, 3, 3], [3]
# Solucion optima: [[5, 5], [4, 3, 3]. [4, 3, 3]]


# Complejidad O(n²)
def bolsasffd(capacidad: int, productos: list[int]) -> list[list[int]]:
    resultado = []
    suma_pesos = []
    ordenados = sorted(productos, reverse=True)
    for producto in ordenados:
        i = 0
        encontrado = False
        while i < len(resultado):
            if suma_pesos[i] + producto <= capacidad:
                resultado[i].append(producto)
                suma_pesos[i] += producto
                encontrado = True
                break
            i += 1
        if not encontrado:
            resultado.append([producto])
            suma_pesos.append(producto)
    return resultado

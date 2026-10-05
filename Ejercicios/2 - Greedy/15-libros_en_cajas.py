# Se tiene una colección de n libros con diferentes espesores, que pueden estar entre 1 y n (valores no necesariamente enteros).
# Tu objetivo es guardar esos libros en la menor cantidad de cajas. Todas las cajas disponibles son de la misma capacidad L (se asegura que L >= n).
# Obviamente, no podés partir un libro para que vaya en múltiples cajas, pero sí podés poner múltiples libros en una misma caja,
# siempre y cuando los espesores no superen esa capacidad L. Implementar un algoritmo Greedy que obtenga las cajas,
# tal que se minimicen la cantidad de cajas a utilizar.
# Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy.
# ¿El algoritmo propuesto encuentra siempre la solución óptima? Justificar.
# ¿Qué cambios aplicarías si supieras que los espesores sólo fueran números enteros? Describir cómo afecta a la complejidad,y a su optimalidad.

# Complejidad: O(n^2), y no es optimo (FFD (First Fit Descending) falla en alguinos casos)
def cajas(capacidad: int, libros: list[float]) -> list[list[float]]:
    ordenados = sorted(libros, reverse=True)  # ordenar de mayor a menor por capacidad
    suma_pesos = []
    resultado = []
    for libro in ordenados:
        i = 0
        encontrado = False
        while i < len(resultado):
            if suma_pesos[i] + libro <= capacidad:
                suma_pesos[i] += libro
                resultado[i].append(libro)
                encontrado = True
                break
            i += 1
        if not encontrado:
            suma_pesos.append(libro)
            resultado.append([libro])
    return resultado

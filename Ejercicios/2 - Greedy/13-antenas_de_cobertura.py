# Tenemos una ruta recta muy larga, de K kilómetros, sobre la cual hay casas dispersas.
# En dichas casas vive gente que usa mucho sus celulares. El intendente a cargo la ruta debe renovar por completo el sistema de antenas,
# teniendo que construir sobre la ruta nuevas antenas. Cada antena tiene un rango de cobertura de R kilómetros (valor constante conocido).
# Implementar un algoritmo Greedy que reciba las ubicaciones de las casas, en número de kilómetro sobre esta ruta (números reales positivos) desordenadas,
# y devuelva los kilómetros sobre los que debemos construir las antenas para que todas las casas tengan cobertura, y se construya para esto
# la menor cantidad de antenas posibles.
# Indicar y justificar la complejidad del algoritmo implementado.
# Justificar por qué se trata de un algoritmo greedy.
# ¿El algoritmo da la solución óptima siempre?

# Regla greedy: Pongo una antena en la casa_actual + R si no supera el limite K, en K si supera, y salteo todas las casas cubiertas

# Optimo local: La antena que quiero poner en la casa_actual + R

# Optimo global: Minimizar la cantidad de antenas puestas


# Complejidad: O(n log n)
def cobertura(casas: list[int], R: int, K: int) -> list[int]:
    resultado = []
    ordenados = sorted(casas)
    i = 0
    while i < len(ordenados):
        if ordenados[i] + R <= K:
            posicion_antena = ordenados[i] + R
        else:
            posicion_antena = K
        resultado.append(posicion_antena)

        while i < len(ordenados) and posicion_antena + R - ordenados[i] >= 0:
            i += 1
    return resultado

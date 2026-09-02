# Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos.
# El listado (ordenado por nombre del pueblo) contiene el número de kilómetro donde está ubicada cada una.
# Se desea ubicar la menor cantidad de patrullas policiales (en las bifurcaciones) de tal forma que no haya bifurcaciones con vigilancia a más de 50 km.
# Justificar que la solución es óptima. Indicar y justificar la complejidad del algoritmo implementado.
# Ejemplo:
# Ciudad 	Bifurcación
# Castelli 	    185
# Gral Guido 	242
# Lezama 	    156
# Maipú 	    270
# Sevigne 	    194

# Si pongo un patrullero en la bifurcación de Lezama, cubro Castelli y Sevigne. Pero no Gral Guido y Maipú.
# Necesitaría en ese caso, poner otro. Agrego otro patrullero en Gral Guido.
# Con eso tengo 2 móviles policiales en bifurcaciones que cubren todas los accesos a todas las ciudades con distancia menor a 50km.

# En un caso alternativo donde solamente se consideren las bifurcaciones de Castelli, Gral Guido y Sevigne, la
# única solución óptima sería colocar un móvil policial en Sevigne.

# Regla greedy: Colocar la patrulla lo mas adelante posible del primer pueblo que no tenga cobertura (manteniendolo vigilado)

# Optimo local: El pueblo donde decido colocar el patrullero

# Optimo global: Minimizar la cantidad de patrulleros colocados manteniendo todas las bifurcaciones vigiladas


def bifurcaciones_con_patrulla(ciudades: list[tuple[str, int]]) -> list[int]:
    resultado = []
    # ordenados de menor a mayor
    ordenados = sorted(ciudades, key=lambda x: x[1])
    i = 0
    while i < len(ordenados):
        alcance_actual = ordenados[i][1] + 50
        # Avanzamos salteando las bifurcaciones que ya estarian cubiertas
        while i < len(ordenados) and alcance_actual - ordenados[i][1] >= 0:
            i += 1
        # Una vez que lleguemos a una no cubierta, ponemos una patrulla en la anterior
        # y actualizamos el alcance
        resultado.append(ordenados[i - 1])
        nuevo_alcance = ordenados[i - 1][1] + 50
        # Ahora salteamos las ciudades cubiertas por la nueva patrulla
        while i < len(ordenados) and nuevo_alcance - ordenados[i][1] >= 0:
            i += 1
    return resultado

# El explorador Roberto se embarcó en una misión para encontrar el legendario Templo de los Vientos. En el vasto desierto, hay oasis
# donde puede recoger provisiones esenciales como agua y comida. Cada oasis tiene recursos limitados. Sin suficientes provisiones,
# Roberto no podrá cruzar el desierto. Sólo vamos a considerar el hecho de tener k cantidad de provisiones (no si son una cosa u otra).
# Implementar un algoritmo greedy que permita a Roberto llegar al templo con la menor cantidad de paradas posibles en los oasis.
# Indicar y justificar la complejidad del algoritmo. Justificar por qué es un algoritmo Greedy. ¿El algoritmo da siempre la solución óptima?
# Si lo hace, justificar, si no dar un contraejemplo.
# Datos que se reciben:
#   Una lista de n elementos que nos indica cuántas provisiones (en cantidad) se pueden conseguir en cada uno de los n oasis.
#   Una lista con las distancias del inicio de la travesía al primer oasis, del primero al segundo, del segundo al tercero, y así hasta el
#   final de la travesía (la lista tiene n + 2 elementos).
#   La cantidad de provisiones iniciales de Roberto.
#   Una constante KM_PROVISION que indica cuántas provisiones se debe consumir para caminar un KM.

# Regla greedy: recargar las provisiones en el oasis mas abundante al momento de no poder avanzar al siguiente oasis

# Optimo local: el oasis que me maximiza la cantidad de provisiones

# Optimo global: minimizar la cantidad de paradas

# Complejidad: O(n log n) siendo n la cantidad de elementos del arreglo distancias
# El while exterior se repite n+1 veces, y por cada iteracion se encola 1 elemento al heap, costando O(log n)
# A lo sumo, se desencolan todos los elementos del heap, costando O(n log n)
# O(n log n) + O(n log n) = O(2(n log n)) = O(n log n)
def menor_cantidad_paradas(cantidad_provisiones: list[int], distancias: list[int], provisiones: int, KM_PROVISION: int) -> list[int]:
    resultado = []
    abundantes = Heap()  # imaginar que es un heap implementado, de maximos, de tuplas (provisiones_oasis, distancia_oasis)
    i = 0
    while i < len(distancias):
        while distancias[i] * KM_PROVISION > provisiones:
            if abundantes.esta_vacio():
                # no se puede atravesar el oasis
                return []
            provisiones_oasis, distancia_oasis = abundantes.desencolar()
            resultado.append(distancia_oasis)
            provisiones += provisiones_oasis
        if i < len(cantidad_provisiones):
            abundantes.encolar((cantidad_provisiones[i], i))
        provisiones -= distancias[i] * KM_PROVISION
        i += 1
    return resultado

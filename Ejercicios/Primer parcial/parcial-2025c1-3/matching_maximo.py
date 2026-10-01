# Dado un grafo sin ciclos (un bosque, el cual es necesariamente bipartito), implementar un algoritmo greedy que obtenga el
# matching máximo. Es decir, el subconjunto máximo de aristas tal que ninguna arista comparta vértice entre sí.
# Indicar y justificar la complejidad del algoritmo. El análisis de la complejidad debe estar completo. Justificar por qué es un
# algoritmo Greedy. ¿El algoritmo da siempre la solución óptima? Si lo hace, justificar, si no dar un contraejemplo.

# Regla greedy: obtener todos los grados de los vertices, encolar los de grado 1 y por cada uno chequear sus adyacentes
# agregando solo a los que no esten presentes en el set de visitados, para luego actualizar el estado actual y ver
# si encolamos o no los adyacentes del adyacente actual

# Optimo local: la arista que me minimiza la cantidad aristas afectadas

# Optimo global: maximizar la cantidad de aristas

# El algoritmo es optimo debido a que se asegura que se elijan las aristas que afecten a la menor cantidad de aristas posibles
# a traves de empezar con los vertices de menor grado e ir actualizando el estado actual de cada uno
def matching_maximo(grafo) -> list:
    resultado = []
    grados = obtener_grados_ordenado(grafo)
    visitados = set()
    cola = Cola()  # imaginar que esta implementado
    # O(V)
    for v, grado in grados.items():
        if grado == 1:
            cola.encolar(v)
    # O(V + E), todos los vertices se llegan a encolar, y a cada le vemos sus aristas,
    # a lo sumo en total 2E entre todos los vertices y hacemos operaciones O(1)
    while not cola.esta_vacia():
        v = cola.desencolar()
        for w in grafo.adyacentes(v):
            if v not in visitados and w not in visitados:
                resultado.append((v, w))
                visitados.add(v)
                visitados.add(w)
                for u in grafo.adyacentes(w):
                    grados[u] -= 1
                    if u not in visitados and grados[u] == 1:
                        cola.encolar(u)
                break
    return resultado


# O(V + E)
def obtener_grados_ordenado(grafo) -> dict:
    grados = {}
    for v in grafo:
        grados[v] = 0
    for v in grafo:
        for w in grafo.adyacentes(v):
            grados[w] += 1
    return grados

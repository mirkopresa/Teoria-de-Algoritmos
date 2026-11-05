# Tenemos un grafo no dirigido que representa una grilla de n x n. Definimos que un vértice en la fila i y columna j es el vértice (i, j).
# Todos los vértices tienen exactamente 4 adyacentes, salvo los de los bordes, es decir los de la primera y última fila o columna.
# Implementar una función que dado el grafo y m puntos iniciales distintos en la grilla (i1, j1), ···, (im, jm), determine si existen m
# caminos disjuntos (de vértices) donde cada uno comience en un punto inicial, y termine en m puntos diferentes del borde. En los
# ejemplos del dorso, el de la izquierda tiene solución (la cuál se muestra) mientras que el de la derecha no tiene solución. Utilizar
# redes de flujo para resolver este problema. Indicar y justificar la complejidad del algoritmo implementado

# O(V*E), siendo V = 2n^2 la cantidad de vertices, ya que creamos por cada vertice un v_in y un v_out
# E = 4n^2 la cantidad de aristas, ya que por cada vertice, a lo sumo creamos 4 aristas (super_fuente -> v_in,
# v_in -> v_out, v_out -> w_in, w_out -> v_in)
# Por que? Crear la red tiene un costo de O(V*E), ya que primero recorremos todos los vertices y agregamos, O(V)
# Luego por cada vertice vemos todos sus adyacentes y hacemos operaciones O(1), O(V + E)
# Y por ultimo recorremos todos los m puntos iniciales, O(m)
# O(V + E) crece mucho mas rapido que O(m)
# Obtener el flujo maximo del grafo nos cuesta O(V*E^2) con la implementacion de BFS
# Pero en este caso, la complejidad final del algoritmo de flujo sera O(V*E)
# Por que?
# El flujo maximo esta acotado por la variable m debido a que la red solo contiene aristas de capacidad 1
# Entonces en cada iteracion, el flujo actual aumentara en 1, y como el flujo maximo posible seria igual a m,
# a lo sumo el algoritmo se repetira m veces, y como maximo podrian haber V = m cantidad de vertices
# Entonces terminamos con complejidad O(V*E)
def caminos_disjuntos_grilla(grafo, puntos_iniciales) -> bool:
    red, s, t = crear_red(grafo, puntos_iniciales)
    flujos = flujo(red, s, t)
    suma_flujo = 0
    for adj in red.adyacentes(s):
        suma_flujo += flujos[(s, adj)]
    return suma_flujo == len(puntos_iniciales)


def crear_red(grafo, puntos_iniciales) -> tuple[Grafo, str, str]:
    red = Grafo(es_dirigido=True)
    red.agregar_vertice("super_fuente")
    red.agregar_vertice("super_sumidero")
    visitados = set()
    for v in grafo:
        red.agregar_vertice(f"{v}_in")
        red.agregar_vertice(f"{v}_out")
    for v in grafo:
        adyacentes = grafo.adyacentes(v)
        v_in = f"{v}_in"
        v_out = f"{v}_out"
        if len(adyacentes) <= 3:
            red.agregar_arista(v_out, "super_sumidero", 1)
        red.agregar_arista(v_in, v_out, 1)
        for w in adyacentes:
            if w not in visitados:
                w_in = f"{w}_in"
                w_out = f"{w}_out"
                red.agregar_arista(v_out, w_in, 1)
                red.agregar_arista(w_out, v_in, 1)
        visitados.add(v)
    for punto in puntos_iniciales:
        red.agregar_arista("super_fuente", f"{punto}_in", 1)
    return red, "super_fuente", "super_sumidero"

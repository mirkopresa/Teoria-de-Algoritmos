# Dada una red y un diccionario que representa los valores de los flujos para las aristas,
# todos valores que respetan la restricción de cada arista, construir la red residual que refleja
# el estado actual de la red en función a los valores de flujo dados.

from grafo import Grafo


def construir_red_residual(grafo: Grafo, flujos: dict) -> Grafo:
    red_residual = Grafo(es_dirigido=True, vertices_init=grafo.obtener_vertices())
    for v in grafo:
        for w in grafo.adyacentes(v):
            flujo = flujos[(v, w)]
            peso_original = grafo.peso_arista(v, w)
            if peso_original > flujo:
                red_residual.agregar_arista(v, w, peso_original - flujo)
            if flujo > 0:
                red_residual.agregar_arista(w, v, flujo)
    return red_residual

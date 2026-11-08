# Shane Hollander e Ilya Rozanov, las dos máximas estrellas y eternos rivales de la liga de hockey sobre hielo, deben organizar durante
# los playoffs la distribución de equipamiento oficial entre las distintas arenas donde se juegan los partidos. Cuentan con un grafo
# dirigido y pesado donde las aristas representan rutas terrestres y su peso indica la capacidad (en bolsos) del camión asignado a ese
# tramo. En cada vértice tenemos un valor w(v) que implica: si es positivo, se trata de un depósito desde el cual se pueden cargar
# hasta esa cantidad de bolsos; si es negativo, se trata de una arena que necesita recibir esa cantidad de bolsos para que se pueda
# disputar el partido; si es 0, es simplemente un punto de trasbordo donde se puede cambiar de camión.
# Usando redes de flujo, implementar un algoritmo que reciba dicho grafo y determine si es posible cumplir con los requisitos de
# todas las arenas. No es necesario indicar cómo serían los traslados. Indicar y justificar la complejidad del algoritmo implementado. El
# análisis de la complejidad debe ser completo.

# Mismo ejercicio que parcial-2025-c2-4
def organizar_equipamiento(ruta_equipamientos: Grafo) -> bool:
    red, adyacentes_ss, s, t = crear_red(ruta_equipamientos)
    flujos = flujo(red, s, t)
    suma_coimas, suma_flujos = 0, 0
    for v in adyacentes_ss:
        suma_coimas -= w(v)
        suma_flujos += flujos[(v, t)]
    return suma_coimas == suma_flujos


def crear_red(ruta_equipamientos: Grafo) -> tuple[Grafo, list[str], str, str]:
    red = Grafo(es_dirigido=True, vertices_init=ruta_equipamientos.obtener_vertices())
    super_fuente = "sf"
    super_sumidero = "ss"
    red.agregar_vertice(super_fuente)
    red.agregar_vertice(super_sumidero)
    adyacentes_ss = []
    for v in ruta_equipamientos:
        peso = w(v)
        if peso == 0:
            continue
        if peso > 0:
            red.agregar_arista(super_fuente, v, peso)
        else:
            adyacentes_ss.append(v)
            red.agregar_arista(v, super_sumidero, -peso)
    for v in ruta_equipamientos:
        for u in ruta_equipamientos.adyacentes(v):
            peso = red.peso_arista(v, u)
            if ruta_equipamientos.estan_unidos(u, v):
                v_intermedio = f"{v} + {u}"
                red.agregar_vertice(v_intermedio)
                red.agregar_arista(u, v_intermedio, peso)
                red.agregar_arista(v_intermedio, v, peso)
            else:
                red.agregar_arista(v, u, peso)

    return red, adyacentes_ss, super_fuente, super_sumidero

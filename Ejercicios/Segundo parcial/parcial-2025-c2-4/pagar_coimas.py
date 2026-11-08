# Tito trabaja para la mafia. Debe llevar en camiones de caudales el dinero recaudado por la organización a modo de devolver favores a
# diferentes estaciones de policía. Entre diferentes rutas puede tener que cambiar de camión (para no ser fácilmente detectado), donde
# cada camión puede tener diferente capacidad. Además, en algunos puntos (escondites de la mafia) puede recoger más dinero.
# Tito entonces cuenta con un grafo dirigido con las diferentes rutas, y puntos donde pueda tener que ir cambiando de camión según
# como cambie de ruta. El grafo es pesado y las aristas tienen como peso la capacidad del camión de caudales a usar por esa ruta. En
# cada vértice tenemos un punto donde podría (o no) poder recoger dinero o tener que dejar un agradecimiento, lo cual está modelado
# con un valor w(v) (si es positivo, al pasar por allí podemos recoger dinero, si es negativo es que debemos dejar un agradecimiento,
# si es 0, es simplemente un punto de cambio de camión y nada más). Tito puede comenzar cada recorrido desde donde desee, si
# bien tiene sentido ir empezando desde algún escondite. Usando redes de flujo, implementar un algoritmo que reciba dicho grafo y
# determine si es posible pagar todos los agradecimientos correspondientes. No es necesario indicar cómo serían los recorridos. Indicar y
# justificar la complejidad del algoritmo implementado. El análisis de la complejidad debe ser completo.

# Planteo de la red
# Super fuente conectada a los escondites con capacidad w(escondite)
# Estaciones de policias conectadas a un super sumidero con capacidad -w(estacion)
# Rompemos aristas antiparalelas
# Lanzamos el flujo, y para que se puedan pagar las coimas, las aristas que se conectan al supersumidero se tienen que saturar

# Complejidad: O(V*E²), siendo V la cantidad de vertices (los escondites, las rutas, y las estaciones policiales + 2), E la cantidad de aristas
# Obtener la red nos cuesta O(V + E) en el peor de los casos, digamos que tenemos todo aristas antiparalelas, vamos a tener
# E + E/2 aristas, que en total seria 3E / 2 = E
# El algoritmo de flujo tiene una complejidad de O(V*E²) en este caso, ya que no se puede aplicar ninguna cota inferior
# Y el ultimo for nos toma como mucho O(V)
# O(V * E²) > O(V + E) > O(V)
def pagar_coimas(ruta_coimas: Grafo) -> bool:
    red, adyacentes_ss, s, t = crear_red(ruta_coimas)
    flujos = flujo(red, s, t)
    suma_coimas, suma_flujos = 0, 0
    for v in adyacentes_ss:
        suma_coimas -= w(v)
        suma_flujos += flujos[(v, t)]
    return suma_coimas == suma_flujos


def crear_red(ruta_coimas: Grafo) -> tuple[Grafo, list[str], str, str]:
    red = Grafo(es_dirigido=True, vertices_init=ruta_coimas.obtener_vertices())
    super_fuente = "sf"
    super_sumidero = "ss"
    red.agregar_vertice(super_fuente)
    red.agregar_vertice(super_sumidero)
    adyacentes_ss = []
    for v in ruta_coimas:
        peso = w(v)
        if peso == 0:
            continue
        if peso > 0:
            red.agregar_arista(super_fuente, v, peso)
        else:
            adyacentes_ss.append(v)
            red.agregar_arista(v, super_sumidero, -peso)
    for v in ruta_coimas:
        for u in ruta_coimas.adyacentes(v):
            peso = red.peso_arista(v, u)
            if ruta_coimas.estan_unidos(u, v):
                v_intermedio = f"{v} + {u}"
                red.agregar_vertice(v_intermedio)
                red.agregar_arista(u, v_intermedio, peso)
                red.agregar_arista(v_intermedio, v, peso)
            else:
                red.agregar_arista(v, u, peso)

    return red, adyacentes_ss, super_fuente, super_sumidero

# Alan y Bárbara están conviviendo en conjunto con n - 2 amigos (es decir, son npersonas conviviendo). Deben organizar quién
# cocinará cada una de las próximas ncenas (una persona debe cocinar sí o sí cada día, obviamente no tiene que ser siempre la misma).
# Hay que considerar que cada persona desea cocinar a lo sumo 2 noches de estas n, y que cada uno de ellos tiene planes que pueden
# hacer que algunas noches no puedan encargarse de la cena. Contando con la información de quién puede cada noche, ¿es posible
# asignar un encargado/a de la cocina para cada una de las noches, sin que nadie cocine más de 2 de estas? ¿Cómo? Implementar
# un algoritmo que, utilizando redes de flujo resuelva el problema (determine si se puede hacer una asignación, y si es así que nos
# indique tal asignación). Indicar y justificar la complejidad del algoritmo implementado en las variables del problema.

# Se tiene un vertice por cada amigo, y un vertice por cada noche
# Se tiene una super fuente con aristas de capacidad 2 a cada amigo, indicando el maximo de noches que pueden cocinar
# Cada noche tiene una arista al super sumidero de capacidad 1, representando si alguien cocino esa noche o no
# Los amigos tienen aristas de capacidad 1 a las noches que desean cocinar, representando si esa noche
# estan disponibles para cocinar o no (y si cocinaron)

# Complejidad del algoritmo: O(V*E²), siendo V la cantidad de amigos n + la cantidad de noches n + 2, y E la cantidad de aristas, que en el peor
# de los casos, todos los amigos querrian cocinar todas las N noches, entonces E = n² + n + n (predomina el n²)
# Reemplazando en la complejidad, nos queda O(n⁵) que es mucho mayor a crear la red (O(n²)), a recorrer todas las noches (O(n))
# y a obtener las asignaciones (O(n²))
def obtener_asignacion(amigos: list[tuple[str, list[str]]]) -> dict | None:
    red, noches, s, t = crear_red(amigos)
    # No se pudieron alcanzar las N noches
    if len(noches) != len(amigos):
        return None
    flujos = flujo(red, s, t)
    for noche in noches:
        if flujos[(noche, t)] == 0:
            return None
    resultado = {}
    for amigo in amigos:
        nombre, _ = amigo
        resultado[nombre] = []
        for noche in red.adyacentes(nombre):
            if flujos[(nombre, noche)] == 1:
                resultado[nombre].append(noche)
    return resultado


def crear_red(amigos: list[tuple[str, list[str]]]) -> tuple[Grafo, set, str, str]:
    super_fuente = "super_fuente"
    super_sumidero = "super_sumidero"
    red = Grafo(es_dirigido=True)
    red.agregar_vertice(super_fuente)
    red.agregar_vertice(super_sumidero)
    noches_vistas = set()
    for amigo in amigos:
        nombre, noches = amigo
        red.agregar_vertice(nombre)
        red.agregar_arista(super_fuente, nombre, 2)
        for noche in noches:
            if noche not in noches_vistas:
                red.agregar_vertice(noche)
                red.agregar_arista(noche, super_sumidero, 1)
                noches_vistas.add(noche)
            red.agregar_arista(nombre, noche, 1)
    return red, noches_vistas, super_fuente, super_sumidero

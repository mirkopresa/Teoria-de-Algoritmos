# Un plan de piso consiste de n interruptores y n luces con sus ubicaciones. Además, un diseño de iluminación es una asignación
# de interruptores y luces (qué luces controla cada interruptor). Un plan de piso es ergonómico si para él existe al menos un diseño de
# iluminación ergonómico. Que un diseño sea ergonómico significa que, para cada interruptor de luz que haya, este maneje una única
# luz (lámpara, lamparita, etc.), y esa luz sea además visible desde el lugar donde está el interruptor. En los ejemplos del
# dorso de este enunciado, el ejemplo de la izquierda es ergonómico, pero el de la derecha no. Implementar, utilizando redes de flujo,
# un algoritmo ergonomicidad(interruptores, luces) que permita determinar si el plan es ergonómico, o no. En caso que lo sea,
# devolver las asignaciones de (interuptor, luz) que correspondan. Suponer que existe una función visible(interruptor, luz)
# que determina si la luz es visible desde el interruptor, y que dicha función ejecuta en tiempo constante. Indicar y justificar la
# complejidad del algoritmo implementado. El análisis de la complejidad debe ser completo.

# Complejidad: O(V * E), siendo V la cantidad de vertices (n + n + 2), E la cantidad de aristas, que en el peor de los casos
# se podran ver todas las luces desde un interruptor, por lo que tendremos (n + n + n²) aristas
# Por que?
# Obtener la red tiene de costo O(V + E), luego chequear si a una luz le llego flujo tiene de complejidad O(V), y obtener la asignacion
# de interruptores con luces tiene por complejidad O(V + E), ya que por cada interruptor, vemos todas sus aristas
# Por ultimo el algoritmo de Ford Fulkerson implementado con BFS en este caso tendra de complejidad O(V * E), debido a que
# todas las aristas tienen capacidad 1, entonces el flujo esta acotado por la variable n, y por cada iteracion, este aumentaria en 1
# hasta llegar a n, y como maximo hay n vertices
# Reemplazando en la variable de entrada, nos queda O(V * E) = O(n³)
def ergonomicidad(interruptores: list[str], luces: list[str]) -> dict | None:
    red, s, t = crear_red(interruptores, luces)
    flujos = flujo(red, s, t)
    for luz in luces:
        if flujos[(luz, t)] != 1:
            return None
    resultado = {}
    for interruptor in interruptores:
        for luz in red.adyacentes(interruptor):
            if flujos[(interruptor, luz)] == 1:
                resultado[interruptor] = luz
    return resultado


def crear_red(interruptores: list[str], luces: list[str]) -> tuple[Grafo, str, str]:
    red = Grafo(es_dirigido=True, vertices_init=interruptores + luces)
    super_fuente = "sf"
    super_sumidero = "ss"
    for interruptor in interruptores:
        red.agregar_arista(super_fuente, interruptor, 1)
    for luz in luces:
        red.agregar_arista(luz, super_sumidero, 1)
    for interruptor in interruptores:
        for luz in luces:
            if visible(interruptor, luz):
                red.agregar_arista(interruptor, luz, 1)
    return red, super_fuente, super_sumidero

# Para poder cortar con el juego del rival, Scaloni cuenta con información precisa minuto a minuto. En un momento dado, tiene la
# información perfecta de qué jugador puede darle un pase a cuál otro (independientemente de quién tenga la pelota) o marcar un gol.
# Scaloni quiere saber a qué jugador, o jugadores, es indispensable marcar para evitar que nos marquen un gol. Suponiendo que una
# jugada arranca en el arquero contrario, y que se tiene la información de qué jugador de ese equipo puede pasarle la pelota a cuál/es
# otro/s (incluyendo al arquero), considerando que esto no es necesariamente recíproco (no todos los jugadores pueden hacer los mismos
# pases o goles, ¿o vos podés dar los mismos pases que Messi?), y cuáles jugadores podrían marcar un gol en ese momento, indicar
# cuáles son los mínimos jugadores contrarios a marcar de tal forma que no sea posible que nos marquen un gol (no podemos marcar
# al arquero). Resolver este problema utilizando redes de flujo. Pueden suponer que la función flujo(red, s, t) les devuelve
# tanto la asignación de flujo a cada arista, como también la Red Residual resultante de aplicar el algoritmo de Ford-Fulkerson. Indicar
# y justificar la complejidad del algoritmo planteado. Para todo el problema, considerar que, si bien hay un único arquero, podrían
# haber n jugadores de campo (simplemente para no quedarse con que son 10 nada más).

from collections import deque


def obtener_jugadores_a_marcar(
    jugadores: list[tuple[str, list[str]]],
    arquero_rival: str,
    goleadores: list[str],
) -> list[str]:
    red, super_fuente, super_sumidero = crear_red(jugadores, arquero_rival, goleadores)
    flujos, red_residual = flujo(red, super_fuente, super_sumidero)
    visitados = bfs(red_residual, super_fuente)
    resultado = []
    for jugador, _ in jugadores:
        if jugador != super_fuente and f"{jugador}_in" in visitados and f"{jugador}_out" not in visitados:
            resultado.append(jugador)
    return resultado


def bfs(grafo, origen: str) -> set:
    visitados = set()
    cola = deque(origen)
    visitados.add(origen)
    while cola:
        v = cola.popleft()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.add(w)
                cola.append(w)
    return visitados


def crear_red(
    jugadores: list[tuple[str, list[str]]],
    arquero_rival: str,
    goleadores: list[str],
) -> tuple[Grafo, str, str]:
    red = Grafo(es_dirigido=True)
    red.agregar_vertice(arquero_rival)
    arquero_aliado = "super_sumidero"
    red.agregar_vertice(arquero_aliado)
    for nombre, _ in jugadores:
        if nombre != arquero_rival:
            nombre_in, nombre_out = f"{nombre}_in", f"{nombre}_out"
            red.agregar_vertice(nombre_in)
            red.agregar_vertice(nombre_out)
            red.agregar_arista(nombre_in, nombre_out, 1)
    for goleador in goleadores:
        if goleador == arquero_rival:
            red.agregar_arista(goleador, arquero_aliado, float("inf"))
        else:
            red.agregar_arista(f"{goleador}_out", arquero_aliado, 1)
    for nombre, pases in jugadores:
        nombre_in, nombre_out = f"{nombre}_in", f"{nombre}_out"
        for pase in pases:
            if nombre == arquero_rival:
                red.agregar_arista(nombre, f"{pase}_in", float("inf"))
            else:
                red.agregar_arista(nombre_out, f"{pase}_in", float("inf"))
    return red, arquero_rival, arquero_aliado

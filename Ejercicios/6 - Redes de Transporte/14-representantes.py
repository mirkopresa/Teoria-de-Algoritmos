# Se está formando una nueva comisión de actividades culturales de un pueblo.
# Cada habitante es miembro de 0 o más clubes, y de exactamente 1 partido político.
# Cada grupo de interés debe nombrar a un representante ante la nueva comisión de actividades culturales, con las siguientes restricciones:
#     cada partido político no puede tener más de n/2 simpatizantes en la comisión,
#     cada persona puede representar a solo un club, cada club debe estar representado por un miembro.
# Implementar un algoritmo que dada la información de los habitantes (a qué clubes son miembros, a qué partido pertenecen),  nos dé una lista de representantes válidos
# (Para RPL, lo volvemos diccionario para que el orden no afecte los resultados de las pruebas, y poder consultar fácilmente).
# Indicar y justificar la complejidad del algoritmo implementado.

# Considerar que la función flujo(red) que implementa el algoritmo de Ford-Fulkerson (usando BFS, definida por Edmonds y Karp)
# ya se encuentra implementada, y devuelve un diccionario con la asignación de flujo que pasa por cada arista de la red definida.

from ff import flujo
from grafo import Grafo


def representantes(miembros: list) -> dict | None:
    super_fuente = "fuente"
    super_sumidero = "sumidero"
    grafo, clubes = crear_grafo_representantes(miembros, super_fuente, super_sumidero)
    flujo_total = flujo(grafo, super_fuente, super_sumidero)
    clubes_vistos = set()
    resultado = {}
    for miembro in miembros:
        for club in miembro.clubes:
            if club in clubes_vistos:
                continue
            for habitante in grafo.adyacentes(club):
                if flujo_total[(club, habitante)] == 1:
                    resultado[habitante] = club
            clubes_vistos.add(club)
    # devolver un diccionario NombreRepresentante -> NombreClubRepresentado
    # si no se puede resolver dadas las características del problema, devolver None
    return resultado if len(resultado) == len(clubes) else None


def crear_grafo_representantes(miembros: list, super_fuente: str, super_sumidero: str) -> tuple[Grafo, list]:
    grafo = Grafo(es_dirigido=True)
    grafo.agregar_vertice(super_fuente)
    grafo.agregar_vertice(super_sumidero)
    partidos = set()
    set_clubes = set()
    for miembro in miembros:
        nombre, clubes, partido_politico = miembro.nombre, miembro.clubes, miembro.partido_politico
        grafo.agregar_vertice(nombre)
        if partido_politico not in partidos:
            grafo.agregar_vertice(partido_politico)
            partidos.add(partido_politico)
        grafo.agregar_arista(nombre, partido_politico, 1)
        for club in clubes:
            if club not in set_clubes:
                grafo.agregar_vertice(club)
                grafo.agregar_arista(super_fuente, club, 1)
                set_clubes.add(club)
            grafo.agregar_arista(club, nombre, 1)
    for partido in partidos:
        grafo.agregar_arista(partido, super_sumidero, len(set_clubes) // 2)
    return grafo, list(set_clubes)

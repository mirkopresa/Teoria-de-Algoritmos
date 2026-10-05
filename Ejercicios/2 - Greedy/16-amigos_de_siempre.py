# El club de Amigos de Siempre prepara una cena en sus instalaciones en la que desea invitar a la máxima cantidad de sus n socios.
# Sin embargo por protocolo cada persona invitada debe cumplir un requisito: Sólo puede ser invitada si conoce a al menos otras 4 personas invitadas.
# Dada un lista de tuplas (duplas) de personas que se conocen:
# a. Nos solicitan seleccionar el mayor número posible de invitados. Proponer una estrategia greedy óptima para resolver el problema.

from grafo import Grafo

# Regla greedy: armar un grafo de invitados con adyacencias entre si, y borrar los vertices que tengan menos de 4 adyacencias
# Repetimos este proceso hasta que ya no hayan vertices para borrar

# Optimo local: el elemento actual que no cumple la cantidad de invitados

# Optimo global: maximizar los invitados


# conocidos: lista de pares de personas que se conocen, cada elemento es un (a,b)
# Complejidad: O(n^2)
def obtener_invitados(conocidos: list[tuple]) -> list:
    resultado = []
    # O(n), siendo n la cantidad de elems de conocidos
    grafo = obtener_grafo_invitados(conocidos)
    # a lo sumo, en cada iteracion, en el peor de los casos, podemos borrar 1 vertice, y asi hasta terminar de borrar todos, osea O(n^2)
    while True:
        borrados = []
        for v in grafo:
            if len(grafo.adyacentes(v)) < 4:
                borrados.append(v)
        if len(borrados) == 0:
            break
        for v in borrados:
            grafo.borrar_vertice(v)
    for v in grafo:
        resultado.append(v)
    return resultado


def obtener_grafo_invitados(conocidos: list[tuple]) -> Grafo:
    personas = set()
    for a, b in conocidos:
        if a not in personas:
            personas.add(a)
        if b not in personas:
            personas.add(b)
    grafo = Grafo(es_dirigido=False, vertices_init=list(personas))
    for a, b in conocidos:
        if not grafo.estan_unidos(a, b):
            grafo.agregar_arista(a, b)
    return grafo

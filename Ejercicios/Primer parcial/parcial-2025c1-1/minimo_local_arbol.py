# Supongamos que contamos con un árbol binario completo. Cada nodo del árbol tiene un valor xi. Todos los xi son valores diferentes.
# Definimos que un nodo v es mínimo local del árbol si su valor es menor al valor de los nodos a los que se conecta (es decir, los hijos
# que tenga y su padre, si tiene). Implementar un algoritmo por división y conquista que obtenga algún mínimo local del árbol en
# O(log n). Justificar apropiadamente la complejidad del algoritmo implementado.
# Considerar que el árbol tiene en su estructura el nombre del nodo, su valor, y las referencias a sus hijos izquierdo y derecho.

# A = 1, B = 2, C = 0, log en base 2 de 1 = 0, 0 = C, -> O(n^c * log n) = O(log n) siendo n la cantidad de nodos del arbol
def minimo_recursivo(padre, nodo_actual) -> int | None:
    # Caso base, el nodo no tiene hijos, comparamos con el padre
    if nodo_actual.izq == None and nodo_actual.der == None:
        if padre is not None:
            if nodo_actual.valor < padre.valor:
                return nodo_actual.valor
            return None
        return nodo_actual.valor

    # Caso normal, comparaciones (no hace falta comparar con el padre porque siempre va a ser menor al nodo actual)
    if nodo_actual.valor < nodo_actual.izq.valor:
        if nodo_actual.der is not None:
            if nodo_actual.valor < nodo_actual.der.valor:
                return nodo_actual.valor
        else:
            return nodo_actual.valor

    menor = None
    # Elegimos el menor nodo para ir por ese camino
    if nodo_actual.der is not None:
        if nodo_actual.izq.valor < nodo_actual.der.valor:
            menor = nodo_actual.izq
        else:
            menor = nodo_actual.der
    else:
        menor = nodo_actual.izq
    posible = minimo_recursivo(nodo_actual, menor)
    return posible

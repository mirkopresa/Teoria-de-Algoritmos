# Patricio es el hermano de Juan (sí, el vago), y tiene una filosofía muy parecida a la de él. El problema es que la lleva a un extremo:
# no le interesa en lo más mínimo el dinero. Si fuera por Patricio, no agarraría la pala ningún día de su vida pero, por mala suerte, la
# vida no es tan sencilla. Su jefe ya le ha llamado la atención, por lo que sabe que no puede estar dos días seguidos sin trabajar. Tiene
# un arreglo de n valores, donde el elemento i indica el esfuerzo de trabajar el día i (cada día demanda un esfuerzo diferente). Patricio
# puede elegir trabajar un día, o no trabajar.
# Implementar un algoritmo que, por programación dinámica, obtenga el mínimo esfuerzo total (suma de esfuerzos) a trabajar en el
# período de n días, con la restricción que Patricio no puede estar dos días seguidos sin trabajar. También escribir el algoritmo que
# permita reconstruir la solución. Indicar y justificar la complejidad del algoritmo implementado (el de programación dinámica, y
# también el de la reconstrucción).

# Casos base:
# Cantidad de trabajos <= 1: [] (no trabaja)
# Cantidad de trabajos == 2: [min(esfuerzos[0], esfuerzos[1])] (trabaja uno de los 2 dias)

# Ecuacion de recurrencia: OPT[i] = min(esfuerzos[i-1] + OPT[i-2], esfuerzos[i] + OPT[i-1])

# Complejidad: O(n), siendo n la cantidad de dias posibles de trabajo
# Recorremos todo el arreglo 1 vez haciendo operaciones O(1)
def patricio_muy_vago(esfuerzos: list[int]) -> list[int]:
    if len(esfuerzos) <= 1:
        return []
    if len(esfuerzos) == 2:
        if esfuerzos[0] < esfuerzos[1]:
            return [0]
        return [1]
    opt = [0] * len(esfuerzos)
    opt[1] = min(esfuerzos[0], esfuerzos[1])
    for i in range(2, len(esfuerzos)):
        opt[i] = min(esfuerzos[i - 1] + opt[i - 2], esfuerzos[i] + opt[i - 1])
    return reconstruccion(opt, esfuerzos)


# O(n), retornar la lista alreves es O(n) y la complejidad del while es <= O(n)
def reconstruccion(opt: list[int], esfuerzos: list[int]) -> list[int]:
    resultado = []
    i = len(opt) - 1
    while i >= 1:
        # Llegamos al caso base
        if i == 1:
            if esfuerzos[1] == opt[1]:
                resultado.append(1)
            else:
                resultado.append(0)
            break
        # Si trabaje hoy, mas el optimo de ayer da el optimo de hoy, trabajamos hoy
        if esfuerzos[i] + opt[i - 1] == opt[i]:
            resultado.append(i)
            i -= 1
        # Si no, si o si trabajamos ayer (para evitar 2 dias sin trabajar), y nos vamos al caso de antes de ayer
        else:
            resultado.append(i - 1)
            i -= 2
    return resultado[::-1]

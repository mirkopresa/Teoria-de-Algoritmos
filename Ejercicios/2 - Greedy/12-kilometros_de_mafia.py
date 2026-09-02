# Trabajamos para el mafioso Arnook, que es quien tiene la máxima influencia y poder en la zona costera de Ciudad República.
# Allí reina el caos y la delincuencia, a tal punto que quien termina organizando las pequeñas mafias locales no es otro sino Arnook.
# En particular, nos vamos a centrar en unos pedidos que recibe de parte de dichos grupos por el control de diferentes kilómetros de la ruta costera.
# Cada pequeña mafia le pide a Arnook control sobre un rango de kilómetros
# (por ejemplo, la mafia nro 1 le pide del kilómetro 1 al 3.5, la mafia 2 le pide del 3.3333 al 8, etc. . . ).
# Si hay una mafia tomando control de algún determinado kilómetro, no puede haber otra haciendo lo mismo (es decir, no pueden solaparse).
# Cada mafia pide por un rango específico. Arnook no cobra por kilómetraje sino por “otorgar el permiso”, indistintamente de los kilómetros pedidos.
# Ahora bien, esto es una mafia, no una ONG, y no debe rendir cuentas con nadie, así lo único que es de interés es maximizar la cantidad de permisos
# otorgados (asegurándose de no otorgarle algún lugar a dos mafias diferentes).
# Implementar un algoritmo Greedy que reciba los rangos de kilómetros pedidos por cada mafia, y determine a cuáles se les otorgará control,
# de forma que no hayan dos mafias ocupando mismo territorio, y a su vez maximizando la cantidad de pedidos otorgados.
# Indicar y justificar la complejidad del algoritmo implementado.
# Justificar por qué el algoritmo planteado es Greedy.
# ¿El algoritmo da la solución óptima siempre?

# Regla greedy: ordenar de menor a mayor por fin, y otorgar el control a las que terminen lo mas antes posible sin que se intersecten

# Optimo local: el rango actual de kilometros

# Optimo global: maximizar la cantidad de pedidos otorgados


# es una reversion del problema de scheduling
# pedidos: lista de tuplas con (km inicio, km fin)
def asignar_mafias(pedidos: list[tuple[int, int]]) -> list[tuple[int, int]]:
    resultado = []
    ordenados = sorted(pedidos, key=lambda x: x[1])
    for rango in ordenados:
        if len(resultado) == 0 or not hay_interseccion(resultado[-1], rango):
            resultado.append(rango)
    return resultado


def hay_interseccion(anterior, posible_nueva):
    return posible_nueva[0] < anterior[1]

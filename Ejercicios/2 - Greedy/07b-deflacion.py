# En Wakanda, tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto.
# Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero Wakanda está atravesando una era de deflación
# y los precios disminuyen todo el tiempo. El precio del producto i el día j+1 es exactamente la mitad del precio en el día j.
# El arreglo R[i] indica todos los precios del primer día. Si bien para reducir costos se debería esperar a que los productos
# sigan bajando, los tiempos de entrega no nos permiten esperar, y cada día debemos comprar uno de los productos.
# Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos.
# Indicar y justificar la complejidad del algoritmo implementado.
# El algoritmo implementado encuentra siempre la solución óptima? Justificar.
# ¿Por qué se trata de un algoritmo Greedy? Justificar


def precios_deflacion(R: list[float]) -> float:
    monto = 0
    factor = 0.5
    ordenado = sorted(R)
    for i in range(len(ordenado)):
        monto += ordenado[i]
        if i + 1 < len(ordenado):
            ordenado[i + 1] = ordenado[i + 1] * factor
        i += 1
        factor *= 0.5
    return monto

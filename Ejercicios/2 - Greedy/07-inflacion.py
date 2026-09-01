# Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto.
# Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero vivimos en una era de inflación
# y los precios aumentan todo el tiempo. El precio del producto i el día j es R[i]^{j + 1} (j comenzando en 0).
# Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos.
# Indicar y justificar la complejidad del algoritmo implementado.
# ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar.
# ¿Por qué se trata de un algoritmo Greedy? Justificar


# Complejidad: O(n log n) al ordenar de mayor a menor

# Regla greedy: ordenar de mayor a menor, y obtener el producto mas caro

# Optimo local: elegir el producto del dia j

# Optimo global: minimizar el costo final)

# Siempre encuentra la solucion optima para este caso, da igual si todos los productos tienen el mismo precio
# o si son miles de productos con precios diferentes


def precios_inflacion(R: list[int]) -> int:
    monto = 0
    j = 0
    precios_ordenados = sorted(R, reverse=True)  # O(n log n)
    for precio_producto in precios_ordenados:  # O(n)
        monto += precio_producto ** (j + 1)
        j += 1
    return monto

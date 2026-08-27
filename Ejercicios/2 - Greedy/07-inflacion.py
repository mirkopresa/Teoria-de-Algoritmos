# Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto.
# Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero vivimos en una era de inflación
# y los precios aumentan todo el tiempo. El precio del producto i el día j es R[i]^{j + 1} (j comenzando en 0).
# Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos.
# Indicar y justificar la complejidad del algoritmo implementado.
# ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar.
# ¿Por qué se trata de un algoritmo Greedy? Justificar


# Complejidad: O(n log n) al ordenar de mayor a menor
# Regla basica: ordenamos de mayor a menor, para cada dia comprar el producto mas caro
# ya que estos son los que mas aumentarian a futuro (optimo local)
# Repetir esto varias veces nos permite llegar al optimo global (en este caso)

# Siempre encuentra la solucion optima mientras todos los productos tengan un precio > 1,
# Caso negativo: el producto ira alternando entre precio negativo y positivo
# Caso entre 0 y 1: el producto reducira cada vez mas su precio o se mantendra igual


def precios_inflacion(R: list[int]) -> int:
    monto = 0
    j = 0
    precios_ordenados = sorted(R, reverse=True)  # O(n log n)
    for precio_producto in precios_ordenados:  # O(n)
        monto += precio_producto ** (j + 1)
        j += 1
    return monto

class Alumno:
    def __init__(self, nombre: str, altura: float):
        self.nombre = nombre
        self.altura = altura


def indice_mas_bajo(alumnos: list[Alumno]) -> int:
    return indice_recursivo(alumnos, 0, len(alumnos) - 1)


def indice_recursivo(alumnos: list[Alumno], inicio: int, fin: int) -> int:
    if inicio == fin:
        return inicio
    mitad = (inicio + fin) // 2
    if alumnos[mitad].altura > alumnos[mitad + 1].altura:
        return indice_recursivo(alumnos, mitad + 1, fin)
    else:
        return indice_recursivo(alumnos, inicio, mitad)


def validar_mas_bajo(alumnos: list[Alumno], indice: int) -> bool:
    if (
        indice != len(alumnos) - 1
        and alumnos[indice].altura < alumnos[indice + 1].altura
    ):
        if alumnos[indice - 1].altura > alumnos[indice].altura:
            return True
    return False

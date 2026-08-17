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


# 1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 1.18, 1.23
alumnos: list[Alumno] = [
    Alumno("Alumno 1", 1.2),
    Alumno("Alumno 2", 1.15),
    Alumno("Alumno 3", 1.14),
    Alumno("Alumno 4", 1.12),
    Alumno("Alumno 5", 1.02),
    Alumno("Alumno 6", 0.98),
    Alumno("Alumno 7", 1.18),
    Alumno("Alumno 8", 1.23),
]

print(indice_mas_bajo(alumnos))
print(validar_mas_bajo(alumnos, 4))
print(validar_mas_bajo(alumnos, 5))

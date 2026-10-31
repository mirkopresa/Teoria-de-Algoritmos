# Supongamos que tenemos un sistema de una facultad en el que cada alumno puede pedir hasta 10 libros de la biblioteca.
# La biblioteca tiene 3 copias de cada libro. Cada alumno desea pedir libros diferentes.
# Implementar un algoritmo que nos permita obtener la forma de asignar libros a alumnos de tal forma que la cantidad de préstamos sea máxima.
# Dar la metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se consigue la máxima cantidad de préstamos.
# ¿Cuál es el orden temporal de la solución implementada?

import ff as flujo
from grafo import Grafo


def cantidad_maxima_prestamos(alumnos: list[str], libros_a_pedir: list[tuple[str, list[str]]], libros: list[str]) -> dict:
    grafo, s, t = crear_grafo_biblioteca(alumnos, libros_a_pedir, libros)
    flujos = flujo(grafo, s, t)
    resultado = 0
    resultado = {}
    for libro in grafo.adyacentes(s):
        for alumno in grafo.adyacentes(libro):
            resultado[alumno] = []
            if flujos[(libro, alumno)] == 1:
                resultado[alumno].append(libro)
    return resultado


def crear_grafo_biblioteca(alumnos: list[str], libros_a_pedir: list[tuple[str, list[str]]], libros: list[str]) -> tuple[Grafo, str, str]:
    grafo = Grafo(es_dirigido=True, vertices_init=alumnos + libros)
    super_fuente = "super_fuente"
    super_sumidero = "super_sumidero"
    grafo.agregar_vertice(super_fuente)
    grafo.agregar_vertice(super_sumidero)
    for alumno in alumnos:
        grafo.agregar_arista(alumno, super_sumidero, 10)
    for libro in libros:
        grafo.agregar_arista(super_fuente, libro, 3)
    for conjunto in libros_a_pedir:
        alumno, libros = conjunto
        for libro in libros:
            grafo.agregar_arista(libro, alumno, 1)
    return grafo, super_fuente, super_sumidero

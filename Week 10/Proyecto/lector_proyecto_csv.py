"""Plantilla para leer el CSV del proyecto."""

import csv
from pathlib import Path


ARCHIVO_CSV = Path(__file__).with_name("proyecto.csv")


def cargar_proyecto(ruta_csv=ARCHIVO_CSV):
    """Devuelve la data del CSV como una lista de diccionarios."""
    proyecto = []

    try:
        with open(ruta_csv, mode="r", encoding="utf-8-sig", newline="") as archivo:
            lector_proyecto = csv.DictReader(archivo)

            for fila in lector_proyecto:
                proyecto.append(fila)

    except FileNotFoundError:
        print(f"No se encontró el archivo de datos: {ruta_csv}")
        raise SystemExit(1)

    return proyecto

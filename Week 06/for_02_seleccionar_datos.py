"""Micro-reto 2: seleccionar datos con for e if.

Contexto: datos ficticios de horas de estudio semanal reportadas en un curso
universitario de UMCA. Se desea identificar los registros de 3 horas o más.

Prediga cuántos registros cumplen la condición antes de completar el ciclo.
"""
#                   0  1  2  4  5
horas_reportadas = [2, 4, 3, 1, 5]
horas_meta = []
cantidad = 0

for horas in horas_reportadas:
    if horas >= 3:
        cantidad += 1
        horas_meta.append(horas)
        # TODO: agregue a horas_meta el dato que cumple la condición.
        

print("Registros que alcanzan la meta:", horas_meta)
print("Cantidad de registros:", len(horas_meta))
print("Cantidad Daniela: ",cantidad)
# Resultado esperado:
# Registros que alcanzan la meta: [4, 3, 5]
# Cantidad de registros: 3

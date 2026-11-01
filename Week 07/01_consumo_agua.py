"""Caso 1: cambio del consumo diario de agua. Complete el programa."""
#                   0    1   2     3   4
consumos_litros = [120, 115, 108, 102, 96]
#         Dia       1    2    3    4    5
# TODO: Calcule el consumo total y el promedio diario.
dias= len(consumos_litros)
consumo_total = sum(consumos_litros)
promedio_diario = consumo_total / dias
# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día.
primer_dia = consumos_litros[0]
ultimo_dia = consumos_litros[-1]
ahorro = primer_dia - ultimo_dia
porcentaje = (ahorro / primer_dia) * 100
# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.
if porcentaje >= 15:
    estado = "Reducción alta"
elif porcentaje > 0:
    estado = "Reducción moderada"
else:
    estado = "Sin reducción"
# TODO: Muestre los cinco resultados.
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.
print("El consumo total de litros es de:", consumo_total)
print("El promedio diario es de:", promedio_diario)
print("El ahorro fue de:", ahorro)
print("La reducción es de:", porcentaje,"%")
print("Estado:", estado)
# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar

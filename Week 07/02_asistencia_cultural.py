"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
limite = capacidad * 0.70
total_asistencias = 0
bloques_supera = 0

for asistencia in asistencias:
    total_asistencias += asistencia
    if asistencia > limite:
        bloques_supera += 1
# TODO: Calcule el promedio y su porcentaje de ocupación.
promedio = (total_asistencias / len(asistencias))
porcentaje_ocupado = (promedio / capacidad) * 100
# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
if porcentaje_ocupado >=80:
    estado= "Alta"
elif porcentaje_ocupado >=50:
    estado = "Media"
else:
    estado = "Baja"
# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.
print("Total de asistencias: ", total_asistencias)
print("El promedio es de: ", promedio)
print("El porcentaje es de: ", porcentaje_ocupado,"%")
print("La cantidad de bloques es de: ", bloques_supera)
print("Su estado es: ", estado)

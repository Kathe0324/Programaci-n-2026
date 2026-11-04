"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).
# TODO: Prepare un acumulador de minutos, un diccionario para contar
#       "Acceso", "Equipo" y "Red", un contador de casos pendientes,
#       un set de provincias con pendientes, una lista de tuplas de casos
#       urgentes y una tupla para el caso con más minutos de atención.
acumulador_minutos = 0
contador = {
    "Acceso" : 0,
    "Equipo" : 0,
    "Red" : 0
}
contador_pendientes = 0
provincias_pendientes = set()
caso_maximo = ()
casos_urgentes = []
# TODO: Recorra incidencias una sola vez. Actualice los acumuladores y el
#       conteo de la categoría de cada registro.
for incidencia in incidencias:
    acumulador_minutos += incidencia["minutos_atencion"]
    contador[incidencia["categoria"]] += 1
# TODO: Si un caso NO está resuelto, cuéntelo y agregue su provincia al set.
#       Si, además, tiene 60 minutos o más, agregue (id, minutos) a la lista
#       de casos urgentes. Actualice la tupla del caso más largo si corresponde.
    if not incidencia["resuelto"]:
        contador_pendientes += 1
        provincias_pendientes.add(incidencia["provincia"])
        if incidencia["minutos_atencion"] >= 60:
            casos_urgentes.append((incidencia["id"],incidencia["minutos_atencion"]))
    if caso_maximo == ():
        caso_maximo = (incidencia["id"],incidencia["minutos_atencion"])
    if incidencia["minutos_atencion"] > caso_maximo[1]:
        caso_maximo = (incidencia["id"], incidencia["minutos_atencion"])
# TODO: Muestre total y promedio de minutos, conteo por categoría, cantidad
#       de pendientes, provincias con pendientes, casos urgentes y caso más
#       largo. Compruebe también si "San Jose" pertenece al set.
# Control: 10 casos; 500 minutos; promedio 50; Acceso 4, Equipo 3, Red 3;
# 4 pendientes en 4 provincias; urgentes INC-02, INC-05 e INC-07;
# más largo INC-07 con 95 minutos; hay pendientes en San Jose.
# Prueba: cambie temporalmente INC-07 a resuelto=True. Debe salir de la
# lista de urgentes, del conteo de pendientes y del set de provincias
# pendientes, pero seguir como caso más largo. Restaure incidencias.py.
promedio = acumulador_minutos / len(incidencias)

print("El total de casos es de: ", len(incidencias))
print("El total de minutos acumulados es de: ",acumulador_minutos)
print("El promedio de minutos es: ", promedio)
print("El conteo de categoría es de: ", contador)
print("Casos Pendientes: ", contador_pendientes)
print("Provincias Pendientes: ", provincias_pendientes)
print("Casos Urgentes: ", casos_urgentes)
print("El caso maximo fue: ",caso_maximo)
print("Hay pendientes en San Jose?: ", "San Jose" in provincias_pendientes)
#El total de casos es de:  10
#El total de minutos acumulados es de:  500
#El promedio de minutos es:  50.0
#El conteo de categoría es de:  {'Acceso': 4, 'Equipo': 3, 'Red': 3}
#Casos Pendientes:  3
#Provincias Pendientes:  {'Limon', 'Guanacaste', 'Cartago'}
#Casos Urgentes:  [('INC-02', 80), ('INC-05', 70)]
#El caso maximo fue:  ('INC-07', 95)
#Hay pendientes en San Jose?:  False
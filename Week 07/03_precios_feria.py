"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]

# TODO: Calcule promedio, mínimo, máximo y rango (máximo - mínimo).
promedio = sum(precios) / len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo
# TODO: Recorra precios con while y un índice para contar los que SUPERAN
#       el promedio. Aumente el índice en cada vuelta para terminar el ciclo.
# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
indice = 0
contador = 0
while indice < len(precios):
    if precios[indice] > promedio:
        contador += 1
indice += 1
if rango >= 300:
    clasificacion = "Variación alta"
elif rango >= 150:
    clasificacion = "Variación moderada"
else:
    clasificacion = "Variación baja"
# TODO: Muestre producto y todos los resultados.
# Con los datos base: promedio ₡980, mínimo ₡850, máximo ₡1200,
# rango ₡350, 2 precios sobre el promedio, variación alta.
print("El producto es: ", producto)
print("El promedio es:", promedio)
print("El mínimo es: ", minimo)
print("El máximo es: ", maximo)
print("El rango es: ", rango)
print("Precios sobre el promedio: ", contador)
print("Su clasificación es:", clasificacion)
# Prueba de código: use temporalmente cinco precios iguales y compruebe que
# el rango sea cero y ninguno supere el promedio. Restaure la lista.
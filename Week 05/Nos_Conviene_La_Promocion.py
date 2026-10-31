# ANALISIS DE PROMOCION
# Producto: Cafe
# Producto: Cafe
# Precio actual: ₡5,000.00
# Unidades actuales: 20
# Ingreso actual: ₡100,000.00
# Descuento: ₡750.00
# Precio promocional: ₡4,250.00
# Aumento esperado en ventas: 20%
# Unidades proyectadas: 24
# Ingreso con promoción: ₡102,000.00
# Diferencia: ₡2,000.00

# RECOMENDACIÓN: lanzar.

producto = ["Cafe", 5000, 20]

# Porcentaje de descuento y aumento de unidades
porcentaje_descuento = 15
porcentaje_aumento = 10

# Calcular el descuento y el precio promocional
descuento = producto[1] * porcentaje_descuento / 100
precio_promocional = producto[1] - descuento

# Calcular el aumento de unidades
aumento_unidades = producto[2] * porcentaje_aumento / 100
unidades_totales = producto[2] + aumento_unidades

# Calcular el ingreso actual
ingreso_actual = producto[1] * producto[2]

# Calcular el ingreso proyectado
ingreso_proyectado = precio_promocional * unidades_totales

# Calcular la diferencia de ingresos
diferencia = ingreso_proyectado - ingreso_actual

# Recomendar si lanzar la promocion
if diferencia > 0:
    lanzar = "Se recomienda lanzar la promocion"
else:
    lanzar = "No se recomienda lanzar la promocion"

# Salida
print("Diferencia de ingresos:", diferencia)
print(lanzar)

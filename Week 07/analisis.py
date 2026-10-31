from sedes import sedes

#Acceso a lista de sedes de emprendimientos
print("Sedes registradas:", len(sedes)) #el len para saber cuandas sedes hay en la lista
print("Primera Sede:", sedes[0]["nombre"])
print("Ventas de la primera sede:", sedes[0]["ventas"])

print("\nAnalisis Semanal de Emprendimientos")

print("\nANÁLISIS SEMANAL DE EMPREDIMIENTOS")

for sede in sedes:
    total = sum(sede["ventas"])
    porcentaje = total / sede['meta'] * 100
    
    #Clasificación
    if porcentaje >= 100:
        estado = "Meta Alcanzada"
    elif porcentaje >= 80:
        estado = "Cerca de la meta"
    else:
        estado = "Requiere atención"
    
    print(
        f"{sede['nombre']} | Total:₡{total:,.2f} | "
        f"Cumpliento: {porcentaje:.2f}% | {estado}"
    )
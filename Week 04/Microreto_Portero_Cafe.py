"""Microreto: el portero del café."""
#Preguntar cuanta energia tiene
#Preguntar si trae cafe
nombre = input("¿Cual es tu nombre?: ").upper().strip()
energia = int(input("¿Cuánta energía tienes de 0 a 100?: "))
trae_cafe = input ("Traes café (si/no)?: ").lower().strip() == 'si'
mensaje = ''

print(trae_cafe)
print(type(trae_cafe))
if trae_cafe:
    print("Viene cargado de café")
    
# Si -50% y no tengo cafe: -> Descansar
if energia < 50 and not (trae_cafe):
    mensaje = 'Ve a descansar'
# # Si 50 % o mas o tenga café: -> Puede ingresar a la clase
elif energia >=50 or trae_cafe:
    mensaje = "Puede ingresar a la clase"
# Cualquier otro escenario: Portero confundido : revisar respuestas

else:
    mensaje = "Portero confundido : revisar respuestas"
    
print (f"{nombre}:{mensaje}")
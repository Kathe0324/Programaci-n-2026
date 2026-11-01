#Saliste a comer pizza con amigos. Llegó la cuenta total y quieren dividirla en partes iguales.
#Entradas
total = float(input('Ingresar el monto de la factura: '))
cantidad_personas = int(input('Ingrese la cantidad de amigos: '))

#Proceso
pago_persona = total / cantidad_personas

#Salida
print('Monto a pagar por amigo: ',pago_persona)
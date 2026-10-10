# TODO: solicita los datos.
# TODO: limpia los textos.
# TODO: convierte los números con try.
# TODO: valida las entradas.
# TODO: aplica las reglas.
# TODO: muestra el resultado.
# #Solución: Misión Kit Seguro

nombre = input("Nombre: ").upper().strip()
kit = input ('Tipo de kit: ').lower().strip()
autorizacion = input ("Tiene autorización (si/no)? ").lower().strip() == 'si'
try:
    cantidad = int(input("Cantidad de Kits?: "))
    if cantidad < 1:
        print("Error: la cantidad minima es 1.")
except ValueError:
        print("Cantidad de Kits invalida, digite del 1 al 100")
        cantidad = -1
try:
    dias = int(input("Días de préstamo?: "))
    if dias < 1:
        print("Error: la cantidad minima es 1.")
except ValueError:
    print("Cantidad de dias invalida, digite del 1 al 31")
    dias = -1
if not nombre or not kit or cantidad < 1 or dias <1:
    resultado = "Registro rechazado: revise los datos ingresados"
elif autorizacion and cantidad <= 3 and  not dias > 7:
    resultado = f"Registro aprobado para {nombre}: {cantidad} kit(s) de {kit}"
else:
    resultado = "Socilitud en revision"

print('\n',"-" * 50,'\n')
print(resultado)



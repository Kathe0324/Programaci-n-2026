#Situacion: Queremos saber en qué año nació una persona basándonos en su edad actual, asumiendo que ya cumplió años en el 2025
#Autor: Katherine Barrantes Sep-25,2026

#anio_actual = 2026
anio = 2026
#print(type(año))
edad = int (input('Ingrese su edad: '))

#Proceso
anio_nacimiento = anio - edad

#Salida
print("Usted nació aproximadamente en: ",anio_nacimiento)

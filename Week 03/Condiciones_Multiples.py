#Leer una nota, si la nota es mayor o igual a 90
#es un Excelente, si la nota es mayor a 80 = Muy bueno
#Si la nota es mayor a 70 = Aprobado,
#Y cualquier nota inferior a 70 = Reprobado

nota = float(input("Ingresa la nota (0-100): "))

if (nota > 100) or (nota < 0):
    print("Error: nota no valida")
else:
    if nota >= 90:
        print("Excelente, Felicidades!!")
    elif nota > 80:
        print("Muy bien!!")
    elif nota >= 70:
        print("Aprobado")
    else:
        print("Reprobado")


    
    
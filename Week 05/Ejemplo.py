#Ejemplo 1
#              0      1    2    3
#mi_lista = ["Kathe", 29, 1.60, True]
#print(mi_lista[1])
#print(type(mi_lista[1]))

#Ejemplo 2. Si cambiamos "x" a "notas / "a" a "suma de notas" / "b" a "promedio"
#    0   1  2
#x = [85,60,98]
#a = sum(x)
#b = a / 3
#print(b)

notas = [85,60,98]
suma_notas = sum(notas)
promedio = suma_notas / 3
if promedio >= 70:
    print("Felicidades aprobo!")
elif promedio >= 60:
    print("Va a convocatoria")
else:
    print("Reprobado")
print(f"El promedio: {promedio:.2f}")
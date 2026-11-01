#Embajada de Python
#Entradas

saldo_bancario = float(input ("Ingrese el monto de su cuenta bancaria: "))
antecedentes = input("Tiene antecedentes penales? Si / No: ")
profesion = input("Cual seria su profesión: ")

#Procesos

if (saldo_bancario >= 50000) and (antecedentes == "no") or (profesion =="diplomatico"):
        print("APROBADO: VISA DORADA")
elif(saldo_bancario >= 20000) and (antecedentes == "no"):
    print("APROBADO: VISA ESTÁNDAR")
elif (saldo_bancario < 20000) and (profesion == "estudiante" or profesion == "jubilado"):
    print("PENDIENTE: Requiere entrevista")
else:
    print("DENEGADO ❌")
    
                
        
    
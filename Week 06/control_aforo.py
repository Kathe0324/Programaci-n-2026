"""Reto integrador: control de ingreso al Anfiteatro del CENAC.

Nombre del estudiante: __________________________________________
Fecha: ____________________

Contexto:
Se analizará el ingreso de grupos a un evento en el Anfiteatro del CENAC, Costa Rica.
Para este ejercicio, use 700 como capacidad del escenario didáctico; no lo presente
como aforo operativo vigente. La ficha de SiCultura indica 700 y las condiciones
del MCJ publicadas en 2023 indican 500, por lo que las fuentes difieren.
SiCultura: https://si.cultura.cr/es/infraestructura/anfiteatro-del-centro-nacional-de-cultura
MCJ (condiciones de uso 2023): https://www.mcj.go.cr/sites/default/files/2023-07/Condiciones%20de%20uso%20de%20las%20instalaciones%20del%20CENAC%202023.pdf

Antes de programar, analice estos casos y complete una traza con ocupación anterior,
decisión y ocupación posterior:
- 650, 60, 50, fin -> acepta 650, rechaza 60, acepta 50; total 700.
- 400, 300, fin -> acepta ambos grupos; total 700.
- 701, fin -> rechaza el grupo; total 0.
- fin -> no hay grupos; total 0.

Traza esperada para 650, 60, 50:
Grupo | Ocupación anterior | Decisión  | Ocupación posterior
650   | 0                  | aceptado  | 650
60    | 650                | rechazado | 650
50    | 650                | aceptado  | 700

Preguntas de análisis:
- ¿Por qué no se conoce cuántas veces se solicitará un grupo?
- ¿Qué lista cambia cuando el grupo se acepta? ¿Y cuando se rechaza?
- ¿Qué no debe cambiar después de un rechazo?
- ¿Qué información puede calcularse al finalizar recorriendo los aceptados?

Objetivo:
Registrar los grupos y evitar que la ocupación supere la capacidad del escenario.

Reglas:
- Cada entrada es un grupo completo. No se permite entrada parcial.
- Escriba "fin" para terminar.
- Acepte solo enteros mayores que cero.
- Si ocupación actual + grupo <= 700, acepte el grupo.
- Si ocupación actual + grupo > 700, rechace el grupo.
- Las entradas inválidas se informan, pero no se cuentan como grupos rechazados por aforo.

Requisitos esenciales:
- Use una lista para grupos aceptados y otra para grupos rechazados.
- Use while para recibir grupos hasta la palabra fin.
- Use append() para guardar el grupo en la lista correspondiente.
- Use condicionales y try-except para decidir y validar cada entrada.
- Use for para calcular el total admitido recorriendo los grupos aceptados.
- Mantenga la ocupación dentro de la capacidad del escenario.
- Muestre ocupación y espacios disponibles después de cada grupo válido.
- Al finalizar, muestre grupos aceptados, grupos rechazados, total admitido
  y espacios disponibles.

Extensiones si hay tiempo:
- Calcule el porcentaje de ocupación.
- Encuentre el grupo aceptado más pequeño y el más grande.
- Clasifique el estado final del recinto.

No use menú, while True, funciones propias, CSV, listas anidadas ni
comprensiones de listas.

Después de cada grupo válido, muestre:
- Mensaje de aceptación o rechazo.
- Ocupación actual.
- Espacios disponibles.

El porcentaje, los extremos de los grupos y el estado final son extensiones;
no son necesarios para completar el objetivo esencial de esta práctica.

Ejemplo de salida completa (incluye indicadores que son extensión):
Entradas: 650, 60, 50, fin

Grupo aceptado: ingresan 650 personas.
Ocupación actual: 650
Espacios disponibles: 50

Grupo rechazado: no hay espacio para 60 personas.
Ocupación actual: 650
Espacios disponibles: 50

Grupo aceptado: ingresan 50 personas.
Ocupación actual: 700
Espacios disponibles: 0

REPORTE FINAL
Grupos aceptados: 2
Grupos rechazados: 1
Personas admitidas: 700
Capacidad máxima: 700
Espacios disponibles: 0
Porcentaje de ocupación: 100.00%
Grupo aceptado más pequeño: 50
Grupo aceptado más grande: 650
Estado final: capacidad completa.

Otros casos para probar:
- Entradas 100, 200, 150, fin -> 450 personas, estado normal.
- Entrada 701, fin -> grupo rechazado, 0 personas admitidas.
- Entrada fin -> reporte sin grupos aceptados.
- Texto, 0 o negativos -> entrada inválida y el programa continúa.
"""


# Desarrolle su solución a partir de esta línea.

grupos_aceptados = []
grupos_rechazados = []
capacidad_maxima = 0

entrada = input("Favor ingrese el numero de grupo de personas (o fin para terminar): ").strip().lower()

while entrada != "fin":
    try:
        grupo = int(entrada)
        capacidad_maxima = capacidad_maxima + grupo
        if capacidad_maxima <= 700: 
            grupos_aceptados.append(grupo)
            print("Grupo aceptado")
            
        else:
            grupos_rechazados.append(grupo)
            capacidad_maxima = capacidad_maxima - grupo
            print("Grupo rechazado")
        print(f"Ocupacion actual: {capacidad_maxima}")
        print("Espacios disponibles: {700 - capacidad_maxima} \n")
    except ValueError:
        grupo = -1
    entrada = input("Favor ingrese el numero de grupo de personas (o fin para terminar): ").strip().lower()

personas_admitidas = 0
for grupos in grupos_aceptados:
    personas_admitidas = personas_admitidas + grupos
    
cantidad_aceptados = len(grupos_aceptados)

print("Reporte Final")
print("-"*10,"\n")
print(f"Grupos aceptados: {cantidad_aceptadas}")
print(grupos_aceptados)
print(grupos_rechazados)
print(personas_admitidas)



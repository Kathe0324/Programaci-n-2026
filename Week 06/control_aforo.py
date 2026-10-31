"""Reto integrador: control de ingreso al Anfiteatro del CENAC.

Nombre del estudiante: Katherine Barrantes
Fecha: Oct 23, 2026

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

# RETO INTEGRADOR: CONTROL DE INGRESO AL ANFITEATRO DEL CENAC
# Nombre: Katherine Barrantes
# Fecha: Oct 23, 2026

grupos_aceptados = []
grupos_rechazados = []
ocupacion_actual = 0
capacidad_maxima = 700

entrada = input("Ingrese el numero de personas del grupo (o fin para terminar): ").strip().lower()

while entrada != "fin":
    try:
        grupo = int(entrada)

        if grupo <= 0:
            print("Entrada invalida: ingrese un entero mayor que cero.")

        elif ocupacion_actual + grupo <= capacidad_maxima:
            grupos_aceptados.append(grupo)
            ocupacion_actual = ocupacion_actual + grupo
            print(f"Grupo aceptado: ingresan {grupo} personas.")

        else:
            grupos_rechazados.append(grupo)
            print(f"Grupo rechazado: no hay espacio para {grupo} personas.")

        if grupo > 0:
            print(f"Ocupacion actual: {ocupacion_actual}")
            print(f"Espacios disponibles: {capacidad_maxima - ocupacion_actual}")
            print()

    except ValueError:
        print("Entrada invalida: escriba un numero entero positivo o fin.")

    entrada = input("Ingrese el numero de personas del grupo (o fin para terminar): ").strip().lower()


# CALCULAR EL TOTAL DE PERSONAS ADMITIDAS
personas_admitidas = 0

for grupo in grupos_aceptados:
    personas_admitidas = personas_admitidas + grupo


# CALCULAR EL REPORTE FINAL
cantidad_aceptados = len(grupos_aceptados)
cantidad_rechazados = len(grupos_rechazados)
espacios_disponibles = capacidad_maxima - ocupacion_actual
porcentaje_ocupacion = (personas_admitidas / capacidad_maxima) * 100

print("\nREPORTE FINAL")
print("-" * 30)
print(f"Grupos aceptados: {cantidad_aceptados}")
print(f"Lista de grupos aceptados: {grupos_aceptados}")
print(f"Grupos rechazados: {cantidad_rechazados}")
print(f"Lista de grupos rechazados: {grupos_rechazados}")
print(f"Personas admitidas: {personas_admitidas}")
print(f"Capacidad maxima: {capacidad_maxima}")
print(f"Espacios disponibles: {espacios_disponibles}")
print(f"Porcentaje de ocupacion: {porcentaje_ocupacion:.2f}%")


# EXTENSIONES: GRUPO MAS PEQUENO Y MAS GRANDE
if cantidad_aceptados > 0:
    grupo_mas_pequeno = grupos_aceptados[0]
    grupo_mas_grande = grupos_aceptados[0]

    for grupo in grupos_aceptados:
        if grupo < grupo_mas_pequeno:
            grupo_mas_pequeno = grupo

        if grupo > grupo_mas_grande:
            grupo_mas_grande = grupo

    print(f"Grupo aceptado mas pequeno: {grupo_mas_pequeno}")
    print(f"Grupo aceptado mas grande: {grupo_mas_grande}")
else:
    print("No hubo grupos aceptados.")


# CLASIFICAR EL ESTADO FINAL
if ocupacion_actual == capacidad_maxima:
    print("Estado final: capacidad completa.")
elif ocupacion_actual > 0:
    print("Estado final: ocupacion normal.")
else:
    print("Estado final: recinto vacio.")


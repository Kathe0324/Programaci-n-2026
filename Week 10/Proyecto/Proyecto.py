"Proyecto Transacciones No Reconocidas."

from lector_proyecto_csv import cargar_proyecto 

proyecto = cargar_proyecto()

def explorar_proyecto(proyecto):
    print("Clientes: ", len(proyecto))
    
def sumar_montos(proyecto):
    total = 0.0
    for fila in proyecto:
        monto_nuevo = float(fila["Monto"].replace("$", "").replace(",", "").strip())
        total += monto_nuevo
    print(f"Monto total de las transacciones no reconocidas: {total:,.2f}")

def contar_procesadores(proyecto):
    conteo = {}
    for fila in proyecto:
        procesador = fila["Procesador"]
        if procesador in conteo:
            conteo[procesador] += 1
        else: conteo[procesador] = 1
        
    print("Procesadores", conteo)

def contar_metodos(proyecto):
    conteo = {}
    for fila in proyecto:
        metodo = fila["Metodo"]
        if metodo in conteo:
            conteo[metodo] += 1
        else: conteo[metodo] = 1
        
    print("Metodos de Pago", conteo)
    
explorar_proyecto(proyecto)
sumar_montos(proyecto)
contar_procesadores(proyecto)
contar_metodos(proyecto)
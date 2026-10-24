"""Micro-reto 3: actualizar una lista por índice con while.

Contexto: puntajes ficticios de una actividad universitaria expresados como
porcentajes. Para un análisis, se transformarán a valores entre 0 y 1.

Prediga la lista final. Complete la actualización y siga el valor del índice.
"""
#           0    1  2    3
puntajes = [72, 85, 90, 100]
indice = 0

#Con For
# for p in puntajes
#  print (puntajes / 100)

#Mientras 0 menor 4
while indice < len(puntajes):
    # TODO: actualice el puntaje de esta posición dividiéndolo entre 100.
    puntajes[indice] = puntajes[indice] / 100
    #print("Seleccion por indice:" , (puntajes [indice]/100)) solo se transforma la mitad de la formula

    indice += 1

print("Puntajes normalizados:", puntajes)

# Resultado esperado: [0.72, 0.85, 0.9]

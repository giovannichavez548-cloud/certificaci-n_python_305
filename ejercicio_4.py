promedio=[.2,8.9,9.9,7.8,10]
#1. Encontrar el promedio mas bajo usando un ciclo for
#suponemos inicialmente que el promedio mas bajo es el primer elemento 
promedio_bajo=promedio[0]
for contador in promedio:
    if contador<promedio_bajo:
        promedio_bajo=contador
    elif contador>promedio_bajo:
        promedio_bajo=contador
print(promedio_bajo)
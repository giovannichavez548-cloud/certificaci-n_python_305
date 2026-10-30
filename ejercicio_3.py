colores=["azul","morado","rojo","amarillo","verde"]
color=input("ingresa el color:")
encontrado=False
for contador in colores:
    print(contador)
    #si el color actual es "rojo", detener el bucle 
    if contador==color:
        print("color encontrado! saliendo del bucle")
        encontrado=True
        break
if not encontrado :
        print("el color,",color," no se encontro")
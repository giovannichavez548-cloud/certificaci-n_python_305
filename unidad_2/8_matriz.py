matriz=[
    [5,8,1],#fila 1 x 3 columnas
    [3,9,2]#fila 2 x 3 columnas
]
#obteniendo el numero total de filas y columnas
filas=len(matriz)
columnas=len(matriz[0])
#ciclo externo para los indices de las filas
for i in range(filas):
    #ciclo interno para los indices de las columnas(J)
    for j in range(columnas):
        print(f"posicion[{i}][{j}]={matriz[i][j]}")

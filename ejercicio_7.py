mapa=[
    [".",".",".","."],
    [".",".",".","."],
    [".",".",".","A"],
    [".",".","B","."]
]
filas=len(mapa)
columnas=len(mapa[0])
#recorriendo la matriz con ciclos anidados
#ciclo externo para manejar filas
for i in range(filas):
    #ciclo externo para manejar columnas
    for j in range(columnas):
        #verificamos si encontyramos el tesoro
        if mapa[i][j]=="A":
            print(f"tesoro encontrado en la posicion [{i}][{j}]")
        if mapa[i][j]=="B":
            print(f"tesoro encontrado en la posicion [{i}][{j}]")

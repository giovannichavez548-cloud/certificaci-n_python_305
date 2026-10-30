matriz = [
    ['A', 'B', 'C'], 
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],  
    ['J', 'K', 'L'],  
    ['M', 'N', 'Ñ'],  
    ['O', 'P', 'Q'],  
    ['R', 'S', 'T'], 
    ['U', 'V', 'W'], 
    ['X', 'Y', 'Z']  
]
filas = 9
columnas = 3

for i in range(filas):
    for j in range(columnas):
        print(f"posicion[{i}][{j}]={matriz[i][j]}")
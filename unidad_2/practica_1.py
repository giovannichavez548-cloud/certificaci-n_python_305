
alumno = []
promedio = []

for i in range(9):
    nombre = input("Nombre del alumno: ")
    calificacion = float(input("Calificacion de 5 a 10: "))

    alumno.append(nombre)
    promedio.append(calificacion)

mayor = promedio[0]
menor = promedio[0]
nombre_mayor = alumno[0]
nombre_menor = alumno[0]

i = 1

while i < 9:
    if promedio[i] > mayor:
        mayor = promedio[i]
        nombre_mayor = alumno[i]

    if promedio[i] < menor:
        menor = promedio[i]
        nombre_menor = alumno[i]

    i = i + 1

print("Promedio mas alto:", mayor)
print("Alumno:", nombre_mayor)
print("Promedio mas bajo:", menor)
print("Alumno:", nombre_menor)

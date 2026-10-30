try:
    alumno = ["Cristian", "geraldine", "santa maria", "giovanni", "jenny", "josafat","michelle","mayte","shantal","yael"]
    calificaciones = [10, 9, 8, 7, 8, 9, 10, 9, 6, 7]
    print(alumno[1], calificaciones[1])
    print(alumno[3], calificaciones[3])
    print(alumno[5], calificaciones[5])
    print(alumno[7], calificaciones[7])
    print(alumno[9], calificaciones[9])
except IndexError:
    print("indice incorecto")
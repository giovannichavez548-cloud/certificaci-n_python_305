#cadenas y concatenacion con(+)
cadena1='HOLA'
cadena2="Mundo"
multilinea=""""esto es una cadena
de varias lineas"""
print(cadena1 + cadena2 + multilinea)
#cadenas y repiticion
eco="ja"*3
print(eco)
#cambiar una cadena de minuscula a mayuscula
tu_nombre='Giovanni'
print(tu_nombre.upper())
#cambiar una cadena de mayusculas a minuscula
print(tu_nombre.lower())
# remplazar texto en cadena
frase="me gusta programacion"
print(frase.replace("programacion","matematicas"))
#formato de concatenar cadenas con valores(f-string)
edad=16
nombre='Giovanni'
mensaje=f"hola, me llamo {nombre}  y tengo \n {edad}años"
print(mensaje)
#contar los caracteres de una cadena
texto="!felicidades por aun continuar en el cecy!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#comprobar si un texto tiene una palabra
oracion="aprender python es divertido"
if"java" in oracion:
    print("encontrado")
else:
 print("no esta")    
# validar contenido de una cadena
ncadena="12"
print(ncadena.isalpha())
print(ncadena.isdigit())

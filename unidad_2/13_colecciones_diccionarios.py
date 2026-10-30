#creando un diccionario en python
persona={
    "nombre":"Giovanni",
    "edad":16,
    "profesion":"chef",
    "estudiante":False
}
print(persona)
#accediendo a un valor en especifico
print(persona["nombre"])
print(persona["profesion"])
#se puede usar el metodo.get() 
#es util porque no da error si la clave no existe
print(persona.get("edad"))
#modificar un valor existente
persona["edad"]=16
print(persona.get("edad"))
#agreggar un par(clave:valor)
persona["ciudad"]="san pepe"
print(persona)
for clave,valor in persona.items():
    print(f"{clave}:{valor}")
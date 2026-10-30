inventario = {
    "lápiz": 10,
    "cuaderno": 5,
    "borrador": 8
}

print("--- INVENTARIO ACTUAL ---")
print(inventario)

producto = input("ingresa el producto: ")
cantidad = int(input("ingresa la cantidad: "))

if producto in inventario:
    if cantidad > 0:
        if cantidad <= inventario[producto]:
            print("venta autorizada")
            inventario[producto] = inventario[producto] - cantidad
            print("--- INVENTARIO ACTUALIZADO ---")
            print(inventario)
        else:
            print("No hay suficiente stock")
    else:
        print("La cantidad debe ser mayor a 0")
else:
    print("El producto no existe en el inventario")

def get_Numero(prompt):
    while True:
        try:
           return int(input(prompt))
        except ValueError:
           print("Debes escribir un el precio como número entero")
PrecioItem = get_Numero("Escriba el valor del producto")
PrecioIva = PrecioItem * 0.19
PrecioTotal = PrecioItem + PrecioIva
print(f"El item a comprar vale {PrecioItem}, el valor del iva es de {PrecioIva}, por lo tanto el precio total es de: {PrecioTotal}")

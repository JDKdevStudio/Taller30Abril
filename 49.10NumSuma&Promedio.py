cantidad, sumatoria, conteo = 0, 0, 0

def get_Numero(prompt):
    while True:
        try:
           return int(input(prompt))
        except ValueError:
           print("Debes escribir un número")

print("Ingrese los valores numericos que desee:")
while True:
    conteo += 1
    x = get_Numero(f"Escriba el número #:{conteo}")
    sumatoria += x
    cantidad += 1
    if conteo == 10:
        promedio = sumatoria / cantidad
        print("la cantidad de valores que digito fue", cantidad)
        print("la sumatoria entre estos valores fue de", sumatoria, "y su promedio fue de", round(promedio))
        break

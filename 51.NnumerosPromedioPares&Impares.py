def get_numero(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Debes escribir un número")
cantidadpar, cantidadimpar, sumatoriapar, sumatoriaimpar = 0, 0, 0, 0
print("Ingrese los valores que desee (presione 0 para terminar)")
print("Al menos ingrese tanto un par como impar")
while True:
    x = get_numero("#= ")
    if x % 2 == 0:
        sumatoriapar += x
    elif x % 2 != 0:
        sumatoriaimpar += x
    if x == 0:
        promediopar = sumatoriapar / cantidadpar
        promedioimpar = sumatoriaimpar / cantidadimpar
        print("la cantidad de valores pares que digito fue", cantidadpar, "y de impares fue", cantidadimpar)
        print("la sumatoria entre estos valores pares fue de", sumatoriapar,
              "y su promedio fue de {0:.2f}".format(promediopar))
        print("por otro lado la sumatoria entre estos valores impares fue de", sumatoriaimpar,
              "y su promedio fue de {0:.2f}".format(promedioimpar))
        break
    if x % 2 == 0:
        cantidadpar += 1
    elif x % 2 != 0:
        cantidadimpar += 1

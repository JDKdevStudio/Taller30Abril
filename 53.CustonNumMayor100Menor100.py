def get_Numero(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Debes escribir un número")
cantidadmas, cantidadigual, cantidadmenos = 0, 0, 0
print("Ingrese los valores que desee (presione 0 para terminar)")
while True:
    try:
        x = get_Numero("#= ")
        if x == 0:
            break
        elif x > 100:
            cantidadmas += 1
        elif x == 100:
            cantidadigual += 1
        else:
            cantidadmenos += 1

    except:
        print("Esa no es una exprecion numerica valida")
print("La cantidad de numeros mayores a 100 fueron", cantidadmas, "y la cantidad menores a 100 fueron", cantidadmenos)
if cantidadigual >= 1:
    print("Ademas se ingresaron", cantidadigual, "numeros iguales a 100")

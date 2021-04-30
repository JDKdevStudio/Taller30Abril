año = int(input("Escriba el año que desea analizar"))

if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")

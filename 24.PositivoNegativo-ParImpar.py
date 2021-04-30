while True:
    numero= int(input("Escribir un numero= "))
    if numero >= 0:
        print("El numero es positivo")
        if numero%2 == 0:
            print("y es par")
        else:
            print("y es impar")
    else:
        print("El numero es negativo")
        if numero%2 == 0:
            print("y es par")
        else:
            print("y es impar")

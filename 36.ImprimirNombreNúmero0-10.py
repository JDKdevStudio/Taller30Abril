from num2words import num2words
while True:
    try:
        num = int(input("Elija un numero entre el 0 y el 10: \n"))
        if num < 0 or num > 10:
            print("Numeros fuera del rango intente de nuevo")
            continue
        else:
            print(num2words(num, lang="es"))
            break
    except:
        print("Ingresa bien los numeros")

while True:
    try:
        num = int(input("Ingresa un numero: "))
        cont = len(str(num))
        if num > 100000:
            print("El numero supera el rango de 100.000")
            continue
        else:
            print("El numero tiene", cont, "digitos")
            break
    except:
        print("Ingresa bien los numeros")

while True:
    try:
        n1, n2, n3 = map(int, input("Ingresa los tres numeros con espacios: \n").split())
        if n2 > n1 & n3 > n2:
            print("la secuencia", n1, n2, n3, "---> esta incrementando")
        elif n1 > n2 & n2 > n3:
            print("la secuencia", n1, n2, n3, "---> esta disminuyendo")
        else:
            print("la secuencia", n1, n2, n3, "---> ni se incrementa ni se disminuyendo")
    except:
        print("Ingresa bien los numeros")

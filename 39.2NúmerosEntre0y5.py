while True:
    try:
        n1, n2 = int(input("Numero 1")), int(input("Numero 2"))
        if n1 in range(0, 6):
            if n2 in range(0, 6):
                print(n1, "y", n2, "--->", True)
        else:
            print(n1, "y", n2, "--->", False)
            break
    except:
        print("Ingresa bien los numeros")

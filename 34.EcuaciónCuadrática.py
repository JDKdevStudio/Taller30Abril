while True:
    try:
        a = float(input("Ingrese a: \n"))
        b = float(input("Ingrese b: \n"))
        c = float(input("Ingrese c: \n"))
        dis = b**2-4*a*c
        if dis < 0:
            print("La ecuacion no tiene soluciones reales")
        elif dis == 0:
            x = -b/(2*a)
            print("La solucion unica es x=","{0:.2f}".format(x))
        else:
            x1 = (-b-(dis**0.5))/(2*a)
            x2 = (-b+(dis ** 0.5)) / (2 * a)
            print("La soluciones reales son x1=", "{0:.2f}".format(x1), "y x2 es=", "{0:.2f}".format(x2))
    except:
        print("Ingresa bien los numeros")

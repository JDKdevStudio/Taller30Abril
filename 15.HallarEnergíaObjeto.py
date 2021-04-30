while True:
    try:
        m = int(input("Ingrese la masa del objeto en kg= "))
        v = float(input("Ingrese la velocidad en m/s= "))
        Ec = (m*v**2)/2
        print("La energia es de", str(Ec) + " Julios")
        break
    except:
        print("Asegurese de poner bien los numeros")

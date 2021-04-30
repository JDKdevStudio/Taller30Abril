while True:
    try:
        s = int(input("Ingrese el tiempo en segundos (enteros)= "))
        a = float(input("Ingrese una aceleracion= "))
        vf = a*s
        print("La velocidad fue de", str(vf) +" m/s")
        break
    except:
        print("Asegurese de poner bien los numeros")

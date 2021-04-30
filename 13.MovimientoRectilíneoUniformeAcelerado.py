while True:
    try:
        t = int(input("Ingrese el tiempo del recorrido en segundos = "))
        v0 = int(input("Ingrese la velocidad actual del objeto en metros sobre segundos = "))
        a = int(input("Ingrese la aceleracion actual del objeto en metros sobre segundos al cuadrado = "))
        vf = v0 + a * t
        x = 0.5 * (vf + v0) * t
        print("La distancia recorrida fue de", x,"metros")
        break
    except:
        print("Asegurese de poner bien los numeros")

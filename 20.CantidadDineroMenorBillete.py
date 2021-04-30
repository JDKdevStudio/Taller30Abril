lista = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
dinero = int(input("Escríba el valor que desea desglosar (sin puntos ni comas)"))
for i in lista:
    if dinero >= i:
        queda = dinero // i
        print(f"Se devuelven {queda} billetes de {i}")
        dinero %= i

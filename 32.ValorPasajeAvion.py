while True:
    try:
        dias, km = int(input("Cuatos dias te vas a quedar en el hotel? \n")), int(input("Y cuantos kilometros el avion recorrio para llegar a tu destino? \n"))
        valor1 = 100000 + (5000*km)
        if km > 1000 and dias > 7:
            descuento = valor1*0.15
            valor2 = valor1-descuento
            print("El valor del ticked es de", str(valor1)+"$", "pero con el descuento es de ahora", str(valor2)+"$")
            break
        else:
            print("El valor del ticked es de", str(valor1)+"$")
            break
    except:
        print("Ingresa bien los valores")

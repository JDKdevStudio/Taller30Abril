import math
lista = []
sumatoria, x = 0, 0
while x != 5:
    try:
        y = int(input("Ingrese el numero que desee: "))
        lista.append(y)
        sumatoria += y
        x+=1
    except:
        print("Asegurese de poner bien los datos")
print("La sumatoria con la funcion sinh fue de", (math.e**sumatoria-math.e**-sumatoria)/2)

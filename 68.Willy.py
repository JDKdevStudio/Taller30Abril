divir = 0
while divir <= 0:
        try:
            print("Ingrese los dos numeros a dividir")
            x = int(input("Dividiendo = "))
            z = int(input("Divisor =  "))
            divir = x/z
            print("La division es ", divir)
            break
        except:
            print("Madre Mía, Willy, no puedes divir por cero")

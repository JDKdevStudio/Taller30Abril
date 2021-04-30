List = []
print("Ingrese los dos numeros")
n1, n2 = int(input("Primero: ")), int(input("Segundo: "))
List.append(n1), List.append(n2)
print("El mayor numero de entre esos dos fue", int(max(List)), "y el menor era ", int(min(List)))

List = []
print("Ingrese tres numeros")
while len(List) != 3:
    x = int(input("#= "))
    List.append(x)
print("El mayor numero de entre esos tres fue", int(max(List)), "y el menor es", int(min(List)))

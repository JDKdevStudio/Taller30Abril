def get_Numero(prompt):
    while True:
        try:
           return int(input(prompt))
        except ValueError:
           print("Debes escribir un número")
n1, n2 = get_Numero("Escriba el primer número"), get_Numero("Ahora escriba el segundo número")
print("La suma de", n1, "y", n2, "es", n1+n2)
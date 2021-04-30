def get_Numero(prompt):
    while True:
        try:
           return float(input(prompt))
        except ValueError:
           print("Debes escribir un número")
n1, n2, n3 = get_Numero("Escriba el número 1"), get_Numero("Escriba el número 2"), get_Numero("Escriba el número 3")
print(f"El promedio de los números {n1}, {n2} y {n3} es:", (n1 + n2 + n3) / 3)

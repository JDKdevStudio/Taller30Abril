def get_Numero(prompt):
    while True:
        try:
           return int(input(prompt))
        except ValueError:
           print("Debes escribir un número")
n1, n2 = get_Numero("Escriba el primer número"), get_Numero("Ahora escriba el segundo número")
print("La suma de ambos números es:", n1 + n2)
print(f"la resta {n1} - {n2} =", n1 - n2, f"y la otra forma puede ser: {n2} - {n1} =", n2 - n1)
print("La multiplicación de ambos números es:", n1 * n2)
print(f"la división {n1} / {n2} =", n1 / n2, f"y la otra forma puede ser: {n2} / {n1} =", n2 / n1)
print(f"el residuo {n1} % {n2} =", n1 % n2, f"y la otra forma puede ser: {n2} % {n1} =", n2 % n1)

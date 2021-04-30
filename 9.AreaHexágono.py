from math import  sqrt
def get_Numero(prompt):
    while True:
        try:
           return float(input(prompt))
        except ValueError:
           print("Debes escribir un número")
Lado = get_Numero("Escríba el valor del lado del hexágono")
print("El área del hexágono es:", 3 * sqrt(3) * Lado**2 / 2)
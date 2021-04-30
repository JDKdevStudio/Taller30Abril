from math import  sqrt
def get_Numero(prompt):
    while True:
        try:
           return float(input(prompt))
        except ValueError:
           print("Debes escribir un número")
Altura = get_Numero("Escríba la altura del objeto en metros")
print("El tiempo de caída en segundos es de:", sqrt(2 * Altura / 9.81))

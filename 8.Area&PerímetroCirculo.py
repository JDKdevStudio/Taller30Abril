import math
def get_Numero(prompt):
    while True:
        try:
           return float(input(prompt))
        except ValueError:
           print("Debes escribir un número")
Radio = get_Numero("Escríba el radio de un círculo")
print("El área es", math.pi * Radio**2, "y el perímetro es", 2 * math.pi * Radio)

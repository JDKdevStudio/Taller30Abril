import math
def get_Numero(prompt):
    while True:
        try:
           return float(input(prompt))
        except ValueError:
           print("Debes escribir un número")
frac, whole = math.modf(get_Numero("Escríba un número decimal"))
print(f"La parte entera es {whole} y la parte decimal es {frac}")

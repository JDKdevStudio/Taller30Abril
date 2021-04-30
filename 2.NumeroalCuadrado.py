def get_Numero(prompt):
    while True:
        try:
           return float(input(prompt))
        except ValueError:
           print("Debes escribir un número")
Numero = get_Numero("Escriba un número para elevar al cuadrado")
print("el número", Numero,"Elevado al cuadrado es", Numero**2)
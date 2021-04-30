def get_Numero(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Debes escribir un número")
x = -1
while x < 0:
    x = get_Numero("Escriba un número positivo")
print(x)

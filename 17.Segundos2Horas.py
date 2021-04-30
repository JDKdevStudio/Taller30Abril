def get_Numero(prompt):
    while True:
        try:
           return int(input(prompt))
        except ValueError:
           print("Debes escribir un número")
seconds = get_Numero("Escriba la cantidad de segundos")
print(f"{seconds} segundos equivalen a {seconds / 3600} horas")

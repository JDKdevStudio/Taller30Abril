def get_Numero(prompt):
    while True:
        try:
           return int(input(prompt))
        except ValueError:
           print("Debes escribir un número")
segundos = get_Numero("Escriba la cantidad de segundos")
horas = segundos // 3600
sobrante1 = segundos % 3600
minutos = sobrante1 // 60
sobrante2 = sobrante1 % 60
print(f"{segundos} segundos representa {horas} horas, {minutos} minutos y {sobrante2} segundos")

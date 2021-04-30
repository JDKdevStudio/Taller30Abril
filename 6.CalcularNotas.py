def get_Numero(prompt):
    while True:
        try:
            Num = float(input(prompt))
            if 0 <= Num <= 5:
                return Num
        except ValueError:
           print("Debes escribir un número")
print("Escribe cada nota correspondiente (su valor debe estar entre 0 y 5)")
n1, n2, n3, n4, n5 = get_Numero("Escriba la nota 1"), get_Numero("Escriba la nota 2"), get_Numero("Escriba la nota 3"), get_Numero("Escriba la nota 4"), get_Numero("Escriba la nota 5")
print("La nota final es de: ", eval(f'{n1}*0.15+{n2}*0.2+{n3}*0.15+{n4}*0.3+{n5}*0.2'))

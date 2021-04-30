def get_Numero(prompt):
    while True:
        try:
            y = int(input(prompt))
            if y > 0:
                return y
        except ValueError:
            print("Debes escribir un número positivo")
conteo, cincos, pares, impares = 0, 0, 0, 0
print("Ingrese los valores que desee")
while True:
    x = get_Numero("#= ")
    conteo += 1
    if x % 2 == 0:
        pares += 1
    if pares == 10:
        break
    if x % 2 != 0:
        impares += 1
    if x == 5:
        cincos += 1
    if cincos == 20:
        break
print("La cantidad de total de numeros fue", conteo, "y el total de pares fueron", pares,
      "mientras que los impares fueron", impares, "y el total de numeros 5 fue", cincos)

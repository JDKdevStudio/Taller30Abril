def get_Numero(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Debes escribir un número")


positivos, negativos, pares, impares, multiplo8 = 0, 0, 0, 0, 0
print("Ingrese los valores que desee (presione 0 para terminar)")
while True:
    x = get_Numero("#= ")
    if x == 0:
        break
    if x > 0:
        positivos += 1
    if x < 0:
        negativos += 1
    if x % 2 == 0:
        pares += 1
    if x % 2 != 0:
        impares += 1
    if x % 8 == 0:
        multiplo8 += 1
print("La cantidad de numeros positivos fue", positivos, "y los negativos fueron", negativos,
      "los numeros pares fueron", pares, "y los impares fueron", impares,
      "y por ultimo los multiplos de 8 fueron", multiplo8)

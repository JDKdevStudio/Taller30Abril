valor1, valor2 = input("Escríba un valor1"), input("Escríba otro valor2")
Aux = valor1
valor1, valor2 = valor2, Aux
print(f"Valor1 antes era {Aux} y ahora es {valor1}. Valor2 antes era {valor1} y ahora es {valor2}")

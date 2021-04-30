def factor(n):
    cant = 0
    for x in range(1, n + 1):
        if n % x == 0:
            cant += 1
    return cant
y = int(input("Ingrese un numero: "))
print(factor(y))

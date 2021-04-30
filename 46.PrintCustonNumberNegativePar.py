n = int(input("Cuantos quiere imprimir= "))
for x in range(1, n + 1):
    if x % 2 == 0:
        x -= x*2
    print(x)

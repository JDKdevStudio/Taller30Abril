n = int(input("Escriba un número natural"))
m = n - 1
while True:
    m = int(input("Escriba un número natural mayor al anterior"))
    if m > n:
        break
for x in range(n, m + 1):
    print(x)

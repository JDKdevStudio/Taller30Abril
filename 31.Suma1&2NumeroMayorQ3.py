n1, n2, n3 = float(input("Escriba el número 1")), float(input("Escriba el número 2")), float(input("Escriba el número 3"))
suma = n1 + n2
if suma > n3:
    print("La suma del primero y el segundo es mayor que el tercer numero")
elif suma == n3:
    print("La suma del primero y el segundo numero es igual al tercer numero")
else:
    print("La suma del primero y el segundo es menor que el tercer numero")

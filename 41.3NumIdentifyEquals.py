x1, x2, x3 = map(int, input("Porfavor digite tres digitos por espacios: \n").split())
if x1 == x2:
    print("El primer y el segundo digito son iguales")
elif x1 == x3:
    print("El primer y el tercer digito son iguales")
elif x2 == x3:
    print("El segundo y el tercer digito son iguales")
elif x1 == x2 and x2 == x3:
    print("Todos los numeros son iguales")
else:
    print("Ninguno de los digitos son iguales")

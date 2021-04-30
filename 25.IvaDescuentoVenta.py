iva = 0.19
while True:
    try:
        p = int(input("Ingrese el valor del producto = "))
        chek = p*iva
        valoriva = p + chek
        if p > 150000:
            des = valoriva*0.05
            valorivanuevo =valoriva - des
            print("Tu compra al superar los 150k se le aplicara un descuento de 5% que equivale a", des)
            print("El valor original del producto es", p, "El iva de este fue de", chek,
                  "y el valor total a pagar con iva es de", valoriva)
            print("Pero al aplicarse el descuento ahora su total es de", str(valorivanuevo)+"$")
            break

        print("El valor original del producto es", p, "El iva de este fue de", chek, "y el valor total a pagar con iva es de", str(valoriva)+"$")
        break
    except:
        print("Asegurese de poner bien el numero")

while True:
    try:
        usuario = str(input("Porfavor digite un usuario: "))
        contra = str(input("Porfavor digite la contraseña: "))
        if usuario == "carlos" and contra == "1234":
            print("Bienvenido de nuevo carlos")
            break
        else:
            print("Contraseña erronea intente de nuevo")
    except:
        print("Ingresa bien los numeros")

Nombre = input("Ingresa tu nombre")
def get_Verbo(prompt):
    while True:
        try:
            return {"true": True, "false": False}[input(prompt).lower()]
        except KeyError:
            print("Solamente puedes escribir true or false")
Verbo = get_Verbo("Cómo te identificas: true (El), false (La)")
Calificativo = input("Ingresa tu calificativo")
if Verbo == True:
    print(Nombre,"El", Calificativo)
else:
    print(Nombre, "La", Calificativo)

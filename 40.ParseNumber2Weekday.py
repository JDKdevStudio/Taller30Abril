import calendar
print("")
while True:
    try:
        dia = int(input("Elija un dia de la semana (entre 1 y 7)= "))
        if dia < 1 or dia > 7:
            print("Esos dias no corresponden a una semana normal")
            continue
        else:
            print(calendar.day_name[dia])
            break
    except:
        print("Ingresa bien los dias")

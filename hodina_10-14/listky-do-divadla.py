cena_osoba = 500

pocet = int(input("Zadej počet lidí: "))

if pocet >= 4:
    cena_celkem = cena_osoba * pocet * 0.75     # skupinová sleva

else:
    vek = float(input("Zadej věk: "))
    if vek >= 65:
        cena_celkem = cena_osoba * pocet * 0.8  # sleva pro seniory
    elif vek < 26:
        student = input("Jste student [ano/ne]: ")
        if student == "ano":
            cena_celkem = cena_osoba * pocet * 0.7
        else:
            cena_celkem = cena_osoba * pocet
    else:
        cena_celkem = cena_osoba * pocet

# sem to skočí po vykonání všech podmínek
print("Cena vstupenky:", cena_celkem / pocet)
print("Cena celková:", cena_celkem)
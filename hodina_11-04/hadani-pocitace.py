print("Mysli si číslo od 1 do 100")
dole = 1
nahore = 100
pokus = 0
moje_odpoved = ""


while moje_odpoved != "s":
    tip = (dole + nahore) // 2
    pokus += 1
    print(f"Můj tip je {tip}")
    print("Napiš mi svojí odpověd: ")
    moje_odpoved = input("")
    if moje_odpoved == "v":
        dole = tip + 1
    elif moje_odpoved == "m":
        nahore = tip - 1
    else:
        print(f"Tvoje číslo je {tip}")
        
print(f"Počet pokusů {pokus}")

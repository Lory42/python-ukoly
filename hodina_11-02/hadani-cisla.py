import random
tajne_cislo = random.randint(1, 20)

tip = 0
pokusy = 0
max_pokusu = 5

print(f"Myslím si číslo od 1 do 20. Hádej mé číslo! Máš na to {max_pokusu} pokusů!")

while tip != tajne_cislo and pokusy < max_pokusu:
    tip = int(input("Zadej svůj tip: "))
    pokusy += 1
    if tip < tajne_cislo:
        print("Moje číslo je VĚTŠÍ!")
    elif tip > tajne_cislo:
        print("Moje číslo je MENŠÍ!")

if tip==tajne_cislo:
    print(f"Gratuluji, uhádl jsi moje číslo {tajne_cislo} na {pokusy} pokusů! :-)")
else:
    print(f"Bohužel ti došly pokusy! Moje tajné čílso je {tajne_cislo}")
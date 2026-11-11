#funkce pro výpočet obsahu obdelníka
def spocitej_obsah(a, b):
    # kontorla platnosti zadaných délek
    if a <= 0 or b <= 0:
        return None
    obsah = a * b
    return obsah
# return a * b

# --- hlavní kód programu ---

print("VÝPOČET ROZLOHY BYTU")
pocet_mistnosti = int(input("Zadej počet místností: "))
mistnost = 1
obsah = 0      #proměnná pro celou výměru bytu (součt dílčích obsahů)
while mistnost <= pocet_mistnosti:
    print(f"Zadej rozměry {mistnost}. místnosti")
    a = int(input("Zadej rozměr \"a\": "))        # pro zvýraznění "a" můžeme buď napsat 'a' nebo \"a\"
    b = int(input("Zadej rozměr \"b\": "))
    obsah_mistnosti = spocitej_obsah(a, b)
    if obsah_mistnosti != None:
        obsah += obsah_mistnosti
        mistnost += 1
print(f"Celková výměra bytu je {obsah}")
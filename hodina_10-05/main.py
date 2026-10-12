# příkaz větvění
x = 0
a = x

if x > 0:
    print("Kladné")
else:
    if (x<0):
        print("Záporné")
        a = -x
    else:
        print("Nula")
# sem směřuji skoky ze všch větví příkazu if

print(f"Abosolutní hodnota čísla {x} je {a}")

if x>0:
    print("Kladné")
elif x<0:
    print("Záporné")
    a = -x
else:
    print("Nula")

cislo = -50
kladne_cislo = cislo > 0
# Číslo 1
# Číslo 2
# Číslo 3
# Číslo 4
# Číslo 5

# 1. Nastavení počáteční hodnoty řídící proměné
pocitadlo = 50

# 2. Cyklus běží, dokud platí podmínka (dokud je pocitadlo rovno 5)
while True:
    print(f"Číslo: {pocitadlo}")
    if pocitadlo == 30:
        break
    pocitadlo -= 1 # Zvýšení hodnoty o 1 (důležité, aby cyklus neskončil v nekonečné smyčce)

print("Konec cyklu")
print(f"Číslo: {pocitadlo}")
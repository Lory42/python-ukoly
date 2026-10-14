xb = int(input("Zadej X souřadnici: "))
yb = int(input("Zadej Y souřadnici: "))

x1_oblast = 5
y1_oblast = 2
x2_oblast = 10
y2_oblast = 7

if lezi_na_1 or lezi_na_2 or lezina_na_3 or lezi_na_4:
    print("Bod leží na hranici oblasti")

elif xb >= x1_oblast and x2 <= x2_oblast and yb >= y1_oblast and yb <= y2_oblast:
     print("Bod leží uvnitř oblasti")

lezi_na_1 = xb >= x1_oblast and xb <= x2_oblast and yb == y1_oblast       #leží na spodní hraně čtverce - je na X od 5 do 10 a na Y je jen 2
lezi_na_2 = yb >= y1_oblast and yb <= y2_oblast and xb == x2_oblast       #leží na pravé hrané čtverce - je na Y od 2 do 7 a na X je jen 10
lezi_na_3 = xb >= x1_oblast and xb <= x2_oblast and yb == y2_oblast
lezi_na_4 = yb >= y1_oblast and yb <= y2_oblast and xb == x1_oblast

if lezi_na_1 or lezi_na_2 or lezina_na_3 or lezi_na_4:
    print("Bod leží na hranici oblasti")

elif xb >= x1_oblast and x2 <= x2_oblast and yb >= y1_oblast and yb <= y2_oblast:
     print("Bod leží uvnitř oblasti")

else:
    print("Bod leží mimo oblast")







a = int(input("Zadej proměnou a: "))
b = int(input("Zadej proměnou b: "))
c = int(input("Zadej proměnou c: "))

# nejprve nastavím, že max i min je proměna a
min = a
max = a

# porovnám s b
if b < min:
    min = b
elif b > max:
    max = b

# porovnám s c
if c < min:
    min = c
elif c < max:
    max = c 

print("Nejmenší číslo", min, "\nNejvětší číslo", max)
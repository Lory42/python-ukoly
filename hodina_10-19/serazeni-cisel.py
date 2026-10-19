a = int(input("Zadej proměnou a: "))
b = int(input("Zadej proměnou b: "))
c = int(input("Zadej proměnou c: "))
p = 10

if a > b:
    p = a
    a = b
    b = p
if b > c:
    p = b
    b = c
    c = p
if a > b:
    p = a
    a = b
    b = p

print(f"{a}, {b}, {c}")



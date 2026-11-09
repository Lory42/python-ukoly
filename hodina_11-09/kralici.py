print("=== SIMULACE PRO CÍSAŘE FRIDRICHA II. ===")
pocet_mesicu = int(input("Zadej počet měsíců simulace: "))

a = 1
b = 1
mesic = 1

while pocet_mesicu != mesic:
    dopredu = a + b
    a = b
    b = dopredu
    mesic += 1
    print(f"Měsíc {mesic}: {dopredu} pár(ů)")

print(f"Na císařském ostrově bude po {pocet_mesicu} měsících celekem {dopredu} párů králíků")


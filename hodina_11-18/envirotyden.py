import urllib.request                       #tečky jsou oddělovače v obktivně orientovaném programování (OOP). Umožňují nám zanořit se do hlavního balíčku (urllib) a vybrat z něj konkrétní podmodul (request) pro práci s webovými adresami.


URL = "https://voskh.cz/envirotyden/index.php?lokalita=kutnahora"

odpoved = urllib.request.urlopen(URL)       # otevření komunikace (uvedení objektu por čtení pomocí https)
den = 0
uhrn_srazek_celkovy = 0

radek = odpoved.readline()                  # přečtení dat řádku


while bool(radek):
    text = radek.decode("utf-8").strip()    #  
    srazka = float(text)
    if srazka >= 0:
        uhrn_srazek_celkovy += 1
        den += 1
    radek = odpoved.readline()

odpoved.close()                             # uzavření komunikace



print("")
print("================================================")
print("   VÝSLEDKY VYHODNOCENÍ SRÁŽEK")
print("================================================")
print(f"Zpracováno dní:         {den}")
print(f"Celkový úhrn srážek:    {uhrn_srazek_celkovy}")
print(f"Průměrný denní úhrn:    {uhrn_srazek_celkovy / den}")
print(f"Průměrný roční úhrn:    {uhrn_srazek_celkovy}")
print("================================================")
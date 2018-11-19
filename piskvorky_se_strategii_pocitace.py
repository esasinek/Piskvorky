from random import randrange

def vyhodnot(kolo):
    "Tato funkce vyhodnotí výsledek zadaného kola."
    if "xxx" in kolo:
        return "x"              #vyhrál uživatel
    elif "ooo" in kolo:
        return "o"              #vyhrál počítač
    elif "-" not in kolo:
        return "!"      #remiza
    else:
        return "-"      #hrajeme dal


def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    return pole[:int(cislo_policka) - 1] + symbol + pole[int(cislo_policka):]


def tah_hrace(pole, symbol):
    spravne_misto = False
    policka = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
    "16", "17", "18", "19", "20"]
    while spravne_misto == False:
        cislo_policka = int(input("Kam chceš hrát? Zadej číslo políčka od 1 do 20.\n"))
        if (str(cislo_policka) in policka) and (pole[cislo_policka - 1] == "-"):
            spravne_misto = True
        else:
            spravne_misto = False
            print("To bohužel nejde.\n")
    herni_pole = tah(pole, cislo_policka, symbol)
    return herni_pole

def tah_pocitace(pole):
    "Vrátí herní pole se zaznamenaným tahem počítače."
    "Počítač se aktivně snaží zabránit výhře protihráče."
    "Podmínky jsou seřazeny podle priority. Počítač se snaží primárně vyhrát."
    "Pokud nelze v daném kole vyhrát, pokusí se aspoň zabránit výhře protihráče."
    symbol = "o"

    if "-oo-" in pole:
        return pole.replace("-oo-", "ooo-", 1)
    elif "o-o" in pole:
        return pole.replace("o-o", "ooo", 1)
    elif "xoo-" in pole:
        return pole.replace("xoo-", "xooo", 1)
    elif "-oox" in pole:
        return pole.replace("-oox", "ooox", 1)
    elif "x-x" in pole:
        return pole.replace("x-x", "xox", 1)
    elif "xx-" in pole:
        return pole.replace("xx-", "xxo", 1)
    elif "-xx" in pole:
        return pole.replace("-xx", "oxx", 1)
    elif "-o-" in pole:
        return pole.replace("-o-", "oo-", 1)
    elif "o--" in pole:
        return pole.replace("o--", "oo-", 1)
    elif "--o" in pole:
        return pole.replace("--o", "-oo", 1)
    else:
        cislo_policka = randrange(20)
        while pole[cislo_policka - 1] == "x" or pole[cislo_policka - 1] == "o":
            cislo_policka = randrange(20)
        return tah(pole, cislo_policka, symbol)



def piskvorky1d():
    "Funkce volá tah hráče a tah počítače, dokud hra neskončí výhrou nebo remízou."
    akt_pole = "--------------------"
    hra = vyhodnot(akt_pole)
    while hra == "-":               # ani vítězství, ani remíza
        akt_pole = tah_hrace(akt_pole, "x")
        hra = vyhodnot(akt_pole)
        if hra != "-":
            break
        print("Pole vypadá takto:", akt_pole, end = "\n")
        print("\nHraje počítač.\n")
        akt_pole = tah_pocitace(akt_pole)
        print("Pole vypadá takto:", akt_pole, end = "\n")
        hra = vyhodnot(akt_pole)
        print()

    if hra == "x":
        print("Pole vypadá takto:", akt_pole, end = "\n")
        vysledek = "Vyhrál jsi!\n"
    elif hra == "o":
        vysledek = "Vyhrál počítač.\n"
    elif hra == "!":
        vysledek = "Remíza.\n"
    print(vysledek)
    return vysledek

print("""
Zahrajeme si hru. 1-D piškvorky se hrají na řádku s dvaceti políčky.

Hráči střídavě přidávají kolečka (`o`) a křížky (`x`), třeba:
1. kolo: -------x------------
2. kolo: -------x--o---------
3. kolo: -------xx-o---------
4. kolo: -------xxoo---------
5. kolo: ------xxxoo---------

Hráč, která dá tři své symboly vedle sebe, vyhrál.

Budeš hrát proti počítači. Ty máš symbol 'x', počítač 'o'.

Hrajeme!
""")
print("Hraješ první. Pole je prázdné: --------------------\n")
piskvorky1d()

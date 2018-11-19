from ai import tah_pocitace
from util import tah

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


def tah_hrace(pole, symbol):
    while True:
        try:
            cislo_policka = int(input("Kam chceš hrát? Zadej číslo políčka od 0 do 19.\n"))
            if pole[cislo_policka] == "-":
                herni_pole = tah(pole, cislo_policka, symbol)
                return herni_pole
        except ValueError:
            print("To bohužel nejde.\n")


def piskvorky1d():
    "Funkce volá tah hráče a tah počítače, dokud hra neskončí výhrou nebo remízou."
    akt_pole = 20 * "-"
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
        vysledek = "Gratuluji! Vyhrál jsi!\n"
    elif hra == "o":
        vysledek = "Je mi líto. Vyhrál počítač.\n"
    elif hra == "!":
        vysledek = "Remíza.\n"
    print(vysledek)
    return vysledek

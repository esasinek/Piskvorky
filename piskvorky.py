from ai import tah_pocitace
from util import tah

def vyhodnot(kolo):
    "Tato funkce vyhodnotí výsledek zadaného kola."
    if "xxx" in kolo:
        return "x"                #vyhrál X
    elif "ooo" in kolo:
        return "o"                #vyhrál O
    elif "-" not in kolo:
        return "!"                #remiza
    else:
        return "-"                #hrajeme dal


def tah_hrace(pole, symbol_hrace):
    while True:
        try:
            cislo_policka = int(input("Kam chceš hrát? Zadej číslo políčka od 0 do 19.\n"))
            if pole[cislo_policka] == "-":
                herni_pole = tah(pole, cislo_policka, symbol_hrace)
                return herni_pole
            else:
                print("Toto pole už je obsazené.")
        except ValueError:
            print("To bohužel nejde.\n")
        except IndexError:
            print("To bohužel nejde.\n")


def piskvorky1d(velikost, symbol_hrace):
    "Funkce volá tah hráče a tah počítače, dokud hra neskončí výhrou nebo remízou."
    akt_pole = velikost * "-"
    hra = vyhodnot(akt_pole)
    while hra == "-":               # ani vítězství, ani remíza
        akt_pole = tah_hrace(akt_pole, symbol_hrace)
        hra = vyhodnot(akt_pole)
        if hra != "-":
            break
        print("Pole vypadá takto:", akt_pole, end = "\n")
        print("\nHraje počítač.\n")
        akt_pole, symbol_pocitace = tah_pocitace(akt_pole, symbol_hrace)
        print("Pole vypadá takto:", akt_pole, end = "\n")
        hra = vyhodnot(akt_pole)
        print()

    if hra == symbol_hrace:
        print("Pole vypadá takto:", akt_pole, end = "\n")
        vysledek = "Gratuluji! Vyhrál jsi!\n"
    elif hra == symbol_pocitace:
        vysledek = "Je mi líto. Vyhrál počítač.\n"
    elif hra == "!":
        vysledek = "Remíza.\n"
    print(vysledek)
    return vysledek

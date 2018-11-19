from random import randrange
from util import tah

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
        return pole.replace("oo-", "ooo", 1)
    elif "-oox" in pole:
        return pole.replace("-oo", "ooo", 1)
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
        while pole[cislo_policka] == "x" or pole[cislo_policka] == "o":
            cislo_policka = randrange(20)
        print("Pole je: {} Číslo políčka je: {}".format(pole, cislo_policka))
        herni_pole = tah(pole, cislo_policka, symbol)
        return herni_pole

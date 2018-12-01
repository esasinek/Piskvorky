from random import randrange
from util import tah

def tah_pocitace(pole, symbol_hrace):
    "Vrátí herní pole se zaznamenaným tahem počítače."
    "Počítač se aktivně snaží zabránit výhře protihráče."
    "Podmínky jsou seřazeny podle priority. Počítač se snaží primárně vyhrát."
    "Pokud nelze v daném kole vyhrát, pokusí se aspoň zabránit výhře protihráče."
    sh = symbol_hrace
    if sh == "x":
        sp = "o"
    else:
        sp = "x"
    try:
        if "-" + sp + sp + "-" in pole:
            vysledne_pole = pole.replace("-" + sp + sp + "-", sp * 3 + "-", 1)
        elif sp + "-" + sp in pole:
            vysledne_pole = pole.replace(sp + "-" + sp, sp * 3, 1)
        elif sh + sp + sp + "-" in pole:
            vysledne_pole = pole.replace(sh + sp + sp + "-", sh + 3 * sp, 1)
        elif "-" + sp + sp + sh in pole:
            vysledne_pole = pole.replace("-" + sp + sp + sh, 3 * sp + sh, 1)
        elif sh + "-" + sh in pole:
            vysledne_pole = pole.replace(sh + "-" + sh, sh + sp + sh, 1)
        elif sh + sh + "-" in pole:
            vysledne_pole = pole.replace(sh + sh + "-", sh + sh + sp, 1)
        elif "-" + sh + sh in pole:
            vysledne_pole = pole.replace("-" + sh + sh, sp + sh + sh, 1)
        elif "-" + sh + "-" in pole:
            vysledne_pole = pole.replace("-" + sh + "-" , sp + sh + "-", 1)
        # elif sh + "--" in pole:                                                   Takhle by nikdy nehrál random :D
        #     vysledne_pole = pole.replace(sh + "--", sh + sp + "-", 1)
        # elif "--" + sh in pole:
        #     vysledne_pole = pole.replace("--" + sh, "-" + sp + sh, 1)
        else:
            cislo_policka = randrange(len(pole))
            while pole[cislo_policka] == "x" or pole[cislo_policka] == "o":
                cislo_policka = randrange(len(pole))
            # print("Pole je: {} Číslo políčka je: {}".format(pole, cislo_policka))                 # test
            vysledne_pole = tah(pole, cislo_policka, sp)
        return vysledne_pole, sp
    except ValueError:
        print("Počítač nemůže hrát na prázdné pole.")

from piskvorky import piskvorky1d, tah_hrace, vyhodnot
from ai import tah_pocitace
from util import tah
import pytest


def test_vyhodnot():
    assert vyhodnot("ooxxxo-xo--x-oo-xx--") == "x"
    assert vyhodnot("--------------------") == "-"
    assert vyhodnot("ooo----xx-----------") == "o"
    assert vyhodnot("xoxoxoxoxoxoxoxoxoxo") == "!"


def test_tah_na_prazdne_pole():
    pole = tah_hrace("--------------------", "x")
    assert len(pole) == 20
    assert pole.count("x") == 1
    assert pole.count("-") == 19


# def test_tah_hrace():

def test_tah_chyba():
    with pytest.raises(ValueError):
        tah_hrace("xoxoxoxoxoxoxoxoxoxo", "x")


def test_delky_pole():
    # pole =
    assert len(pole) == 20


def test_ruzne_delky_pole():
    pole = "-x-xox"
    assert tah_pocitace == "-xoxox"


# def tah_hrace(pole, symbol):
#     spravne_misto = False
#     policka = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
#     "16", "17", "18", "19", "20"]
#     while spravne_misto == False:
#         cislo_policka = int(input("Kam chceš hrát? Zadej číslo políčka od 1 do 20.\n"))
#         if (str(cislo_policka) in policka) and (pole[cislo_policka - 1] == "-"):
#             spravne_misto = True
#         else:
#             spravne_misto = False
#             print("To bohužel nejde.\n")
#     herni_pole = tah(pole, cislo_policka, symbol)
#     return herni_pole

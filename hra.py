import piskvorky


print("""
Zahrajeme si hru. 1-D piškvorky se hrají na řádku s dvaceti políčky.

Hráči střídavě přidávají kolečka (`o`) a křížky (`x`), třeba:
1. kolo: -------x------------
2. kolo: -------x--o---------
3. kolo: -------xx-o---------
4. kolo: -------xxoo---------
5. kolo: ------xxxoo---------

Hráč, která dá tři své symboly vedle sebe, vyhrál.

Budeš hrát proti počítači.
""")

while True:
    symbol_hrace = input("Jakým chceš hrát symbolem?")
    if symbol_hrace == "x" or symbol_hrace == "o":
        print("Super. Hrajeme!")
        print("Hraješ první. Pole je prázdné: --------------------\n")
        piskvorky.piskvorky1d(20, symbol_hrace)
    elif symbol_hrace == "konec":
        break
    else:
        print("To nejde. Vyber si symbol 'x' nebo 'o'.")

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

Budeš hrát proti počítači. Ty máš symbol 'x', počítač 'o'.

Hrajeme!
""")
print("Hraješ první. Pole je prázdné: --------------------\n")


piskvorky.piskvorky1d(20)

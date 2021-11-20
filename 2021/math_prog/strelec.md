# Střelec

Tento soubor popisuje třetí úkol olympiády v programování. Pro zpracování jsem se rozhodl použít python abych dokázal nasimulovat proces hledání.

## Šachovnice

Základem bylo vymyslet jak budou jednotlivé dílky šachovnice rozděleny. Nejlepším řešením mi vyšlo dvojrozměrné pole.

př.:
```py

šachovnice = [
    ["A", "B", "C"],
    ["D", "A", "X"],
]

```

Prvním indexem pole získám všechny prvky na souřadnici x a druhým konkrétní prvek z této souřadnice.

V programu to tedy vypadá takto:

```py
board_height, board_width = input("").split(" ")[0:2] # Uživatel zadá výšlu a šířku šachovnice
word = input("") # Uživatel zadá slovo které chce hledat na šachovnici 
board = [] # Inicializace proměnné pro šachovnici

max_height = int(board_height) - 1 # Maximální bod kterého lze dosáhnout na souřadnici y 
max_width = int(board_width) - 1 # Maximální bod kterého lze dosáhnout na souřadnici x

first_char = word[0] # První znak slova
paths = [] # Inicializace pole pro ukládání všech nalezených cest šachové figurky
word = word[1:] # Nastavení zbytku slova do proměnné word

```

## Hledání prvního písmena

Dalším krokem bylo najít souřadnice každého dílku na kterém je počáteční písmeno. To jsem udělal tak, že jsem přes for cyklus prohledal každý řádek a v něm i každý prvek řádku. Pokud byl prvek roven prvnímu písmenu, uložil jsem jeho souřadnici do pole `paths`. Pokud nedojde k nalezení žádného čísla, program se ukončí a vypíše 0.

```py
for height in range(len(board)): # Smyčka prochází každý řádek, v pomocné proměnné height je vždy číslo řádku
    for width in range(len(board[height])): # Smyčka prochází každý prvek řádku, v pomocné proměnné width je číslo prvku v řádku
        if board[height][width] == first_char: # Pokud je hodnota na šachovnici rovna prvnímu znaku, dojde k uložení
            paths.append([[height, width]])

if not paths: # Pokud nenalezne první písmeno ani jednou, program se hned ukončí
    print("0")
    exit()

```

## Hledání dalších písmen

Po tom, co jsem našel písmena (tedy potenciální cesty), bylo potřeba hledat další písmena. Vpodstatě jsem pro každé hledal takové souřadnice na kterých bylo ono písmeno. Vytvořil jsem pole, které obsahovalo souřadnice potenciálních míst (takových která vedou po diagonálách a nejsou mimo šachovici). V tomto poli jsem potom rozhodl, zda na souřadnici skutečně je daný znak. Pokud ano, uložil jsem ho k předchozím prvkům. Toto opakuji tak dlouho dokud jdou vyhledat potenciální místa. Jakmile jsem našel všechny cesty pro dané písmeno, z pole cest jsem smazal cesty, které už nebudou potřeba (takové, které nemají prvky posledního hledání-pro další hledání by byly zbytečné).

```py
for char_index in range(len(word)): # Cyklus všech písmen slova 
    for path_index in range(len(paths)): # Cyklus všech dosud existujících cest 
        path = paths[path_index] # Cesta aktuálního cyklu
        point = path[-1] # Souřadnice aktuálního cyklu
        distance = 1 # Vzdálenpost od bodu
        posibilities = [ # Pole možností, kde pokud se nejde pohybovat po diagonále dál, bude hodnota [] 
            [point[0]+distance, point[1]+distance] if point[0] < max_height and point[1] < max_width else [],
            [point[0]-distance, point[1]-distance] if point[0] > 0 and point[1] > 0 else [],
            [point[0]+distance, point[1]-distance] if point[0] < max_height and point[1] > 0 else [],
            [point[0]-distance, point[1]+distance] if point[0] > 0 and point[1] < max_width else [],
        ]
        while posibilities != [[], [], [], []]: # Dokud se lze stále pohybovat
            for posibility in posibilities: # Kontrola možností
                if not posibility: # Musí existovat (nesmí být prázdné pole)
                    continue
                if posibility == point: # Nesmí být rovna výchozí souřadnici
                    continue
                if board[posibility[0]][posibility[1]] == word[char_index]: # Pokud je na souřadnicích aktuální znak, dojde k uložení celé cesty
                    temp = path.copy()
                    temp.append(posibility)
                    paths.append(temp)
            
            distance+= 1 # Zvětšení vzdálenosti
            last= distance-1 # Poslední bod
            posibilities = [ # Možnosti pohybu po diagonále
                [point[0]+distance, point[1]+distance] if point[0]+last < max_height and point[1]+last < max_width else [],
                [point[0]-distance, point[1]-distance] if point[0]-last > 0 and point[1]-last > 0 else [],
                [point[0]+distance, point[1]-distance] if point[0]+last < max_height and point[1]-last > 0 else [],
                [point[0]-distance, point[1]+distance] if point[0]-last > 0 and point[1]+last < max_width else [],
            ]

    temp = [] 
    for path_index in range(len(paths)): # Zrušení nepotřebných cest
        if char_index+2 == len(paths[path_index]):
            temp.append(paths[path_index])

    paths = temp
```

## Zakončení

Nakonec stačilo vrátit zbytek po dělení velikosti pole cest číslem 10^9+7.

```py
print(len(paths) % (10**9 + 7))
```

## Výsledný kód

```py
board_height, board_width = input("").split(" ")[0:2]
word = input("")
board = []

max_height = int(board_height) - 1
max_width = int(board_width) - 1

for rows in range(int(board_height)):
    cols = list(input(""))
    board.append(cols)

first_char = word[0]
paths = []
word = word[1:]

for height in range(len(board)):
    for width in range(len(board[height])):
        if board[height][width] == first_char:
            paths.append([[height, width]])


if not paths:
    print("0")
    exit()

for char_index in range(len(word)):
    for path_index in range(len(paths)):
        path = paths[path_index] 
        point = path[-1]
        distance = 1
        posibilities = [
            [point[0]+distance, point[1]+distance] if point[0] < max_height and point[1] < max_width else [],
            [point[0]-distance, point[1]-distance] if point[0] > 0 and point[1] > 0 else [],
            [point[0]+distance, point[1]-distance] if point[0] < max_height and point[1] > 0 else [],
            [point[0]-distance, point[1]+distance] if point[0] > 0 and point[1] < max_width else [],
        ]
        while posibilities != [[], [], [], []]:
            for posibility in posibilities:
                if not posibility:
                    continue
                if posibility == point:
                    continue
                if board[posibility[0]][posibility[1]] == word[char_index]:
                    temp = path.copy()
                    temp.append(posibility)
                    paths.append(temp)
            
            distance+= 1
            last= distance-1
            posibilities = [
                [point[0]+distance, point[1]+distance] if point[0]+last < max_height and point[1]+last < max_width else [],
                [point[0]-distance, point[1]-distance] if point[0]-last > 0 and point[1]-last > 0 else [],
                [point[0]+distance, point[1]-distance] if point[0]+last < max_height and point[1]-last > 0 else [],
                [point[0]-distance, point[1]+distance] if point[0]-last > 0 and point[1]+last < max_width else [],
            ]

    temp = []
    for path_index in range(len(paths)):
        if char_index+2 == len(paths[path_index]):
            temp.append(paths[path_index])

    paths = temp

print(len(paths) % (10**9 + 7))
```

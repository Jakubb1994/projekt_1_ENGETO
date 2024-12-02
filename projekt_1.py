'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jakub Prajzler
email: prajzler25@gmail.com

'''
text = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Registrovaní uživatelé
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Přihálšení uživatele
uzivatelske_jmeno = input("Zadej uživatelské jméno:\n")
heslo = input("Zadej heslo:\n")

if uzivatelske_jmeno in uzivatele and uzivatele[uzivatelske_jmeno] == heslo:
    print(f"Vítej v aplikace, {uzivatelske_jmeno}!")
    print(f"Máme 3 texty, které je třeba analyzovat.")
else:
    print("Neregistrovaný uživatel, konec programu.")
    exit()
    
# Výběr textu
vyber = input("Pro výběr textu zadej číslo v rozmezí 1 až 3:\n")
if vyber.isdigit() and 1 <= int(vyber) <= 3:
    vyber = int(vyber)      # Převod na číslo, pokud je vstup platný
else:
    print("Neplatný vstup, konec programu.")
    exit()

# Výběr textu
vybrany_text = text[vyber - 1]

# Analýza textu
slova = vybrany_text.split()

pocet_slov = len(slova)
velka_pismena_zacatek = sum(1 for slovo in slova if slovo.istitle())
pouze_velka_pismena = sum(1 for slovo in slova if slovo.isupper())
pouze_mala_pismena = sum(1 for slovo in slova if slovo.islower())
pocet_cisel = sum(1 for slovo in slova if slovo.isdigit())
soucet_cisel = sum(int(slovo) for slovo in slova if slovo.isdigit())

# Výsledek analýzy
print("-" * 43)
print(f"Vybraný text obsahuje {pocet_slov} slov.")
print(f"Slova začínající velkým písmenem: {velka_pismena_zacatek}.")
print(f"Slova psaná velkými písmeny: {pouze_velka_pismena}.")
print(f"Slova psaná malými písmeny: {pouze_mala_pismena}.")
print(f"Počet čísel v textu: {pocet_cisel}.")
print(f"Součet všech čísel v textu: {soucet_cisel}.")
print("-" * 43)



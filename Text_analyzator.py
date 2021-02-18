'''
author = Jiri Drahotsky
'''
TEXTS = ['''
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

users = {}
users['bob'] = '123'
users['ann'] = 'pass123'
users['mike'] = 'password123'
users['liz'] = 'pass123'

jmeno = input('Username: ')
heslo = input('Password: ')

users_name = users.keys()

print(50*'-')
prihlaseni = False
for name in users_name:
    if name == jmeno:
        if users[name] == heslo:
            prihlaseni = True
            print(f'Welcome to the app, {jmeno}')
        else:
            prihlaseni = True
            print('Password is incorrect')
            exit()

if prihlaseni == False:
    print('User is not registered')
    exit()

print(50*'-')
print('We have 3 texts to be analyzed:')
text_cislo = input('Enter a number btw. 1 and 3 to select:')

# kontrola zadani spravne hodnoty testu (1 - 3)
if not text_cislo.isdecimal:
    print('No number entered')
    exit()
elif text_cislo == 0 and text_cislo > 3:
    print('Number must be in range 1 to 3')
    exit()
else:
    print(f'Text number {text_cislo} has been chosen')

text_cislo = int(text_cislo) - 1

jednotliva_slova = TEXTS[text_cislo].split()

vycistena_slova = []
for slovo in jednotliva_slova:
  vycistena_slova.append(slovo.strip(".,!?"))
pocet_slov = len(vycistena_slova)


velke_pismeno = 0
velka_pismena = 0
mala_pismena = 0
pocet_cisel = 0
soucet = 0
for slovo in vycistena_slova:
  # počet slov začínajících velkým písmenem
  if slovo.isalpha() == True and slovo[0] == slovo[0].title():
        velke_pismeno = velke_pismeno + 1

  # Velka pisemena
  if slovo.isalpha() == True:
    if slovo == slovo.upper():
        velka_pismena += 1

  #Mala pisemena
    if slovo == slovo.lower():
        mala_pismena = mala_pismena + 1

  #pocet cisel a soucet
  if slovo.isdecimal() == True:
      pocet_cisel = pocet_cisel + 1
      soucet = soucet + int(slovo)


# zjisteni cetnosti slov
cetnost_slov = {}
for slovo in vycistena_slova:
    delka_slova = len(slovo)
    cetnost_slov[delka_slova] = cetnost_slov.setdefault(delka_slova, 0) + 1

#zobrazeni vysledku
print(40 * "-")
print(f'There are {pocet_slov} words in the selected text.')
print(f'There are {velke_pismeno} titlecase words.')
print(f'There are {velka_pismena} uppercase words.')
print(f'There are {mala_pismena} lowercase words.')
print(f'There are {pocet_cisel} numeric strings.')
print(f'The sum of all the numbers {soucet} ')

print(40 * "-")
print('LEN|   OCCURENCY   |NR')
print(40 * "-")

# serazeni
cetnost_serazeni = {}
for i in sorted(cetnost_slov):
    cetnost_serazeni[i] = cetnost_slov[i]

# tisk
for i in cetnost_serazeni:
    hvezdicky = cetnost_serazeni.get(i) * "*"
    print(f'{i}| {hvezdicky} | {cetnost_serazeni.get(i)}')
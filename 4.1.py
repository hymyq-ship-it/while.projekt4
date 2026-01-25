#Kirjoita -toistorakennetta käyttävä ohjelma,
# joka tulostaa kolmella jaolliset luvut väliltä 1..1000.whilen
luku = 1

while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku += 1

numero = 2
while numero <= 200:
    if numero % 2 == 0:
        print(numero)
    numero += 1
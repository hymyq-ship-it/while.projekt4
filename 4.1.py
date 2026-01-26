#Kirjoita -toistorakennetta käyttävä ohjelma,
# joka tulostaa kolmella jaolliset luvut väliltä 1..1000.whilen
luku = 1
while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku += 1
#helpomppi tapa tehdä tämä koodi
luku=3
while luku <= 999:
    print(luku)
    luku += 1

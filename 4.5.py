#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

salasana= "sala"
käyttäjätynnys = "huma"
yritys= 1
käyttäjä= input("Anna käyttäjätunnuksen: ")
salasana= input("Anna salasana: ")

while (käyttäjätynnys != käyttäjä or salasana != salasana) and yritys <5:
    print(" väärät tiedot on syötetty")
    yritys = yritys+1
    käyttäjä = input("Anna käyttäjätunnuksen: ")
    salasana = input("Anna salasana: ")
if salasana=="sala" and käyttäjätynnys== "huma":
    print("Tervetuloa ")
else:
    print("et pääse")

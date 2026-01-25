import random

salainen = random.randint(1, 10)

arvaus_str = input("Arvaa luku 1-10: ")

# Muutetaan ensimmäinen arvaus numeroksi, jos se ei ole tyhjä
if arvaus_str != "":
    arvaus = int(arvaus_str)
else:
    arvaus = -1

# Silmukka jatkuu niin kauan kuin arvaus on väärä JA syöte ei ole tyhjä
while arvaus != salainen and arvaus_str != "":
    if arvaus > salainen:
        print("Liian suuri arvaus")
    elif arvaus < salainen:
        print("Liian pieni arvaus")

    # Kysytään uusi arvaus
    arvaus_str = input("Arvaa luku 1-10: ")
    if arvaus_str != "":
        arvaus = int(arvaus_str)

# Kun silmukka loppuu, tarkistetaan miksi
if arvaus_str == "":
    print("Peli keskeytetty.")
else:
    print("Oikein.")



import random

# Kysytään arpakuutioiden määrä
maara = int(input("Kuinka monta arpakuutiota heitetään? "))

summa = 0

# Heitetään arpakuutiot
for i in range(maara):
    heitto = random.randint(1, 6)
    summa += heitto

# Tulostetaan tulos
print("Silmälukujen summa on:", summa)

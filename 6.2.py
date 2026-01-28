import random
def heita_noppa(tahkot):
    return random.randint(1, tahkot)
tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))

print("Heitetään noppaa kunnes saadaan maksimi:", tahkojen_maara)

while True:
    silmaluku = heita_noppa(tahkojen_maara)
    print("Heitto:", silmaluku)
    if silmaluku == tahkojen_maara:
        break

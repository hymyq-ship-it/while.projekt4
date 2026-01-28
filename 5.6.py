kaupungit = []

# Kysytään viisi kaupungin nimeä
for i in range(5):
    nimi = input("Anna kaupungin nimi: ")
    kaupungit.append(nimi)

# Tulostetaan nimet allekkain
print("Kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)

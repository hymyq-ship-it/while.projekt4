luvut = []

# Kysytään lukuja kunnes käyttäjä antaa tyhjän merkkijonon
while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    luvut.append(int(syote))

# Lajitellaan luvut suurimmasta pienimpään
luvut.sort(reverse=True)

# Tulostetaan viisi suurinta
print("Viisi suurinta lukua:")
for luku in luvut[:5]:
    print(luku)

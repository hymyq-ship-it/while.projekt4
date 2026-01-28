
def poista_parittomat(luvut):
    karsittu = []
    for luku in luvut:
        if luku % 2 == 0:      # jos luku on parillinen
            karsittu.append(luku)
    return karsittu

# Pääohjelma
alkuperainen = [3, 8, 11, 4, 7, 10, 2]

karsittu_lista = poista_parittomat(alkuperainen)

print("Alkuperäinen lista:", alkuperainen)
print("Karsittu lista (vain parilliset):", karsittu_lista)

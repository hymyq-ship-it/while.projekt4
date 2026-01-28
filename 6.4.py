# Funktio, joka palauttaa listan lukujen summan
def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

# Pääohjelma
lista = [3, 7, 10, -2, 5]   # Testilista

tulos = laske_summa(lista)
print("Listan lukujen summa on:", tulos)

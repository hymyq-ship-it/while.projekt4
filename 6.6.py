import math

#laskee pizzan yksikköhinnan euroina per neliömetri
def pizzan_yksikkohinta(halkaisija_cm, hinta_euro):
    sade = halkaisija_cm / 2
    pinta_ala_m2 = math.pi * (sade ** 2) / 10000   # cm² → m²
    yksikkohinta = hinta_euro / pinta_ala_m2
    return yksikkohinta

# Pääohjelma
print("Anna ensimmäisen pizzan tiedot:")
halkaisija1 = float(input("Halkaisija (cm): "))
hinta1 = float(input("Hinta (€): "))

print("\nAnna toisen pizzan tiedot:")
halkaisija2 = float(input("Halkaisija (cm): "))
hinta2 = float(input("Hinta (€): "))

# Lasketaan yksikköhinnat
yks1 = pizzan_yksikkohinta(halkaisija1, hinta1)
yks2 = pizzan_yksikkohinta(halkaisija2, hinta2)

print(f"\nPizza 1 yksikköhinta: {yks1:.2f} €/m²")
print(f"Pizza 2 yksikköhinta: {yks2:.2f} €/m²")

# Verrataan
if yks1 < yks2:
    print("Pizza 1 antaa paremman vastineen rahalle.")
elif yks2 < yks1:
    print("Pizza 2 antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat yhtä edullisia.")

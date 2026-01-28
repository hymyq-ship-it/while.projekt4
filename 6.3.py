# Funktio, joka muuntaa gallonat litroiksi
def gallonat_litroiksi(gallonat):
    return gallonat * 3.785


# Pääohjelma
while True:
    gallonat = float(input("Anna bensiinimäärä (gallonoina, negatiivinen lopettaa): "))

    if gallonat < 0:
        print("Ohjelma päättyy.")
        break

    litrat = gallonat_litroiksi(gallonat)
    print(f"{gallonat} gallonaa on {litrat:.3f} litraa")

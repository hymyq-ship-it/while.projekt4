def laske_kolmio_ala(kanta, korkeus):
    ala=(kanta*korkeus)/2
    return ala
# ei oi käyttä suora (ala) laskemisesta voi käyttä kun ne ovat funktionin sisällä
#eli et voi kirjoitta print("f{ala}") tämä on väärin!

ka=float(input("Anna kanta"))
ko=float(input("Anna korkeu"))
tulos=laske_kolmio_ala(ka,ko)
print(tulos)
#Hyvä esimeki

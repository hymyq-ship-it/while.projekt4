onkotyhjä= True
lukustr= input("anna luku:")
if lukustr!= "":
    lukuint = int(lukustr)
    suurin=lukuint
    pienin=lukuint
    onkotyhjä= False
while lukustr!="":
    if lukuint >suurin:
        suurin = lukustr
    if lukuint <pienin:
        pienin = lukuint

    lukustr = input("anna luku:")
    if lukustr != "":
        lukuint = int(lukustr)

if onkotyhjä == False:
    print(suurin, pienin)
else:
    print("et antanut numero")
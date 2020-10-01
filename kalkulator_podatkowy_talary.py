#author: GRAD
#data: 03.04.2020

dochod = float(input("Wprowadz roczny dochod: "))
prog_podatku = 85528
kwota_podatku = 0

if(dochod <= prog_podatku):  #pierwszy prog podatkowy
    kwota_podatku= (0.18*dochod) - 556.2
else:
    kwota_podatku = 14839.2 + (0.32*(dochod-prog_podatku))

if (kwota_podatku < 0): #kwota podatku nie moze byc < 0
    kwota_podatku = 0.0

    
kwota_podatku = round(kwota_podatku, 0)
print("Podatek wynosi: ", kwota_podatku, "talarow")


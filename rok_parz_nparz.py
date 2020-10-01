rok = int(input("Wprowadź rok: "))

if(rok < 1582):
    print("Nie w kalendarzu gregoriańskim")
elif(rok % 4 != 0):
    print("Rok", rok, "jest rokiem zwykłym, ma 365 dni.")
elif(rok % 100 == 0):
    if(rok % 400 == 0):
        print("Rok", rok, "jest przestepnym ma 366dni.")
    else:
        print("Rok", rok, "jest rokiem zwykłym, ma 365 dni.")
else:
     print("Rok", rok, "jest przestepnym ma 366dni.")

c0 = 0
count = 0
while(c0 <= 0):
    c0 = int(input("Podaj dowolna nieujemna i niezerowa liczbe: "))
    if(c0 <= 0):
        print("Podales liczbe niespelniajaca tego wymogu! Sprobuj ponownie.")

while(c0 != 1):
    count += 1
    if(c0 % 2 == 0): ##liczba c0 jest parzysta
        c0 = c0 / 2
    else:            ##liczba c0 jest nieparzysta
        c0 = 3*c0 +1
    print(c0)

print("liczba krokow: ", count)


        

    

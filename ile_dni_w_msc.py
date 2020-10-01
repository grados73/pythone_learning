def czy_przestepny(rok):
    if(rok % 4 == 0):
        if(rok % 100 == 0):
            if(rok % 400 ==0):
                return True
            return False
        return True
    return False

def dni_w_miesiacu(rok, miesiac):
   if(1 <=rok<=3000 and 1<=miesiac<=12): ##warunki brzegowe dla parametrow
        t_dni= [[1, 31], [2, 28], [3, 31], [4, 30], [5, 31], [6, 30],
                    [7, 31], [8, 31], [9, 30], [10, 31], [11, 30], [12, 31]]
        if czy_przestepny(rok): ##rok przestpeny
            t_dni[1][1] = 29
        else:  ##rok nieprzestepny
            t_dni[1][1] = 28
        return t_dni[miesiac-1][1]
        #print(t_dni[miesiac-1][1])
   #else:
    #    return None


testuj_lata = [1900, 2000, 2016, 1987]
testuj_miesiace = [2, 2, 1, 11]
testuj_wynik = [28, 29, 31, 30]
#ile_dni=dni_w_miesiacu(2000,3)
#print(ile_dni)
for i in range(len(testuj_lata)):
	r = testuj_lata[i]
	m = testuj_miesiace[i]
	print(r, m, "-> ", end="")
	wynik = dni_w_miesiacu(r, m)
	if wynik == testuj_wynik[i]:
		print("OK:", wynik, "dni")
	else:
		print("Nie powiodło się", wynik, "dni")

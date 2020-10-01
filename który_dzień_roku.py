def czy_przestepny(rok):
#
    if(rok % 4 == 0):
        if(rok % 100 == 0):
            if(rok % 400 ==0):
                return True
            return False
        return True
    return False
#

def dni_w_miesiacu(rok, miesiac):
#
    if(1 <=rok<=3000 and 1<=miesiac<=12): ##warunki brzegowe dla parametrow
            t_dni= [[1, 31], [2, 28], [3, 31], [4, 30], [5, 31], [6, 30],
                        [7, 31], [8, 31], [9, 30], [10, 31], [11, 30], [12, 31]]
            if czy_przestepny(rok): ##rok przestpeny
                t_dni[1][1] = 29
            else:  ##rok nieprzestepny
                t_dni[1][1] = 28
            return t_dni[miesiac-1][1]
    else:
        return None
#

def dzien_w_roku(rok, miesiac, dzien):
    suma_dni=0
    for i in range(miesiac-1):
        suma_dni = suma_dni + dni_w_miesiacu(rok,i+1)
    suma_dni= suma_dni + dzien
    return suma_dni


ile_dni=dni_w_miesiacu(2000,3)
print(ile_dni)
print(dzien_w_roku(1900, 11, 1))

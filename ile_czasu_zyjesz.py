##author: Grad
##date:12.04.2020
##Description:Program pobiera Twoja date urodzenia i aktualna date oraz oblicza ile czasu zyjesz,
##uwzgledniajac przy tym lata przestepne

##Pobiera rok i zwraca True/False w zaleznosci czy rok jest przestepny
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

##pobiera rok i miesiac i zwraca ilosc dni w danym miesiacu
##lub None gdy ktoras z wartosci nie spelnia warunkow brzegowych dla parametrow
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
##ile minelo dni od 1 sycznia br do dnia dzisiejszego
def dzien_w_roku(rok, miesiac, dzien): ##liczy dni w danym roku do obecnego dnia
    suma_dni=0
    for i in range(miesiac-1):
        suma_dni = suma_dni + dni_w_miesiacu(rok,i+1)
    suma_dni= suma_dni + dzien
    return suma_dni

##ile minelo dni w latach od rok_ur+1 do rok_dzis-1 wlacznie
def dni_w_latach(rok_ur, rok_dzis):
    suma_dni = 0
    for i in range(rok_ur+1, rok_dzis, 1):
        if czy_przestepny(i):
            suma_dni += 366
        else:
            suma_dni += 365
    return suma_dni

##ile minelo dni od ur do konca roku ur
def dni_w_roku_ur(rok, miesiac, dzien):
    suma_dni = 0
    for i in range(miesiac+1, 13, 1):
        suma_dni += dni_w_miesiacu(rok,i)
    suma_dni += (dni_w_miesiacu(rok,miesiac)-dzien)
    return suma_dni

##Pobieranie danych dot urodzenia
dzien_ur = int(input("Podaj dzien urodzenia: "))
miesiac_ur = int(input("Podaj miesiac urodzenia: "))
rok_ur = int(input("Podaj rok urodzenia: "))
print("Urodziles sie ", dzien_ur, "-go ", miesiac_ur, " ", rok_ur, " roku.", sep="")
dzien_dzis=12
miesiac_dzis=4
rok_dzis=2020

#pobieranie danych dot aktualnej daty
print("Czy dzis jest: ", dzien_dzis, ".", miesiac_dzis, ".", rok_dzis,"r. [t/n]", sep="")
warunek_daty = input()

if warunek_daty != "t":
    dzien_dzis = int(input("Podaj dzisiejszy dzień: "))
    miesiac_dzis = int(input("Podaj miesiac aktualny(1-12): "))
    rok_dzis = int(input("Podaj rok aktualny: "))

##ile minelo dni od 1 sycznia br do dnia dzisiejszego
ilosc_dni_w_br = dzien_w_roku(rok_dzis, miesiac_dzis, dzien_dzis)
##ile minelo dni w latach od rok_ur+1 do rok_dzis-1 wlacznie
ilosc_dni_pomiedzy_latami = dni_w_latach(rok_ur, rok_dzis)
##ile minelo dni od ur do konca roku ur
ilosc_dni_r_ur = dni_w_roku_ur(rok_ur, miesiac_ur, dzien_ur)

ilosc_dni_zycia = ilosc_dni_w_br + ilosc_dni_pomiedzy_latami + ilosc_dni_r_ur

ilosc_lat = rok_dzis-rok_ur-1
ilosc_dni_bez_lat = ilosc_dni_w_br + ilosc_dni_r_ur
if(ilosc_dni_bez_lat >= 365):
    ilosc_lat += 1
    ilosc_dni_bez_lat -=365


print("Żyjesz", ilosc_lat, "lat", "i", ilosc_dni_bez_lat, "dni.")
print("To aż", ilosc_dni_zycia, "pełnych dni życia.")
print("Co daje", ilosc_dni_zycia*24, "godzin.")
print("Co daje", ilosc_dni_zycia*24*60,"minut.")
print("Co daje", ilosc_dni_zycia*24*60*60,"sekund.")

klasa = {}

while True:
    imie = input("Wprowadź imię studenta i naciśnij klawisz Enter, żeby przerwać wprowadzanie: ")
    if imie == 'exit':
        break
    
    wynik = int(input("Wprowadź wynik uzyskany przez studenta (0-10): "))
    
    if imie in klasa:
        klasa[imie] += (wynik,)
    else:
        klasa[imie] = (wynik,)
        
for imie in sorted(klasa.keys()):
    suma = 0
    licznik = 0
    for wynik in klasa[imie]:
        suma += wynik
        licznik += 1
    print(imie, ":", suma / licznik)

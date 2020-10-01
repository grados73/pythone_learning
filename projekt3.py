blokow = int(input("Wprowadź liczbę bloków: "))
#
wysokosc = 0
suma = 0


# Napisz tutaj swój kod.

while (suma <= blokow):
    suma = suma + wysokosc
    if(suma > blokow):
        continue
    wysokosc += 1
#	
print("Wysokość piramidy wynosi:", wysokosc-1)

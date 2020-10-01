tajnyNumer = 777

print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")
liczba = int(input("Wprowadź liczbę całkowitą: "))

while (liczba != tajnyNumer):
    print("Nie, to nie jest ta liczba, którą wybrałem dla ciebie. Spróbuj ponownie!")
    if (liczba < tajnyNumer):
        print("Dam Ci podpowiedz, to wieksza liczba.")
    else:
        print("Dam Ci podpowiedz, to mniejsza liczba.")
    liczba = int(input("Wprowadź liczbę całkowitą: "))

print("Dobra robota! To numer, który wybrałem dla ciebie! Jesteś teraz wolny.")
#

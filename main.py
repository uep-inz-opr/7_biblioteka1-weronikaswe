import ast

biblioteka = dict()

class Ksiazka:
    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok
        self.egzemplarze = 0
    def tytul(self) -> str:
        return self.tytul()
    def autor(self) -> str:
        return self.autor()
    def rok(self) -> int:
        return self.rok()
    def egzemplarze(self):
        return self.egzemplarze()
    def dodaj_ksiazke(self):
        if (self.tytul, self.autor) not in biblioteka:
            biblioteka[(self.tytul, self.autor)] = 1
            self.egzemplarze += 1
        else:
            self.egzemplarze += 1


liczba_egzemplarzy = input()
for i in range(int(liczba_egzemplarzy)):
    dane_egzemplarza = eval(input())
    ksiazka = Ksiazka(dane_egzemplarza[0], dane_egzemplarza[1], dane_egzemplarza[2])
    ksiazka.dodaj_ksiazke()
    print((ksiazka.tytul, ksiazka.autor, ksiazka.egzemplarze))


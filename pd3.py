import itertools
## ZAD 1
print("******* ZAD 1 *******")
class material:
    def __init__(self,x,y,z):
        self.rodzaj = x
        self.dlugosc = y
        self.szerokosc = z
    def wyswietl_nazwe(self):
        print(self.rodzaj)


class ubrania(material):
    rozmiar = "M"
    kolor = "czerwony"
    dla_kogo = "k"
    def wyswietl_dane(self):
        print(self.rozmiar)
        print(self.kolor)
        print(self.dla_kogo)

class sweter(ubrania):
    rodzaj_swetra = "rozpinany"
    def wyswietl_dane(self):
        print(self.rodzaj_swetra)

test = sweter("dres",10,20)
test.wyswietl_nazwe()
test.wyswietl_dane()
test2 = ubrania("dres",20,10)
test2.wyswietl_dane()

## ZAD 2
print("******* ZAD 2 *******")

class Ksztalty:
    def __init__(self, x, y):
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik

class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x

    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)
    def __add__(self,other):
        sumx = self.x + other.x
        return Kwadrat(sumx)
    def __ge__(self,other):
        return self.x >= other.x
    def __gt__(self,other):
        return  self.x > other.x
    def __le__(self,other):
        return  self.x <= other.x
    def __lt__(self,other):
        return self.x < other.x

kw = Kwadrat(5)
kw2 = Kwadrat(10)
print(kw)
print(kw2)
kw3 = kw2+kw
print(kw3)

## ZAD 3
print("******* ZAD 3 *******")

print(kw >= kw2)
print(kw > kw2)
print(kw <= kw2)
print(kw < kw2)

## ZAD 4
print("******* ZAD 4 *******")

class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstruktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
p2 = Point(1,1)

print(p1.counter)
print(p2.counter)
print("--------------")
p1.update(1)
print(p1.counter)
print(p2.counter)
print("--------------")
p2.update(1)
print(p1.counter)
print(p2.counter)
print("--------------")
p3 = Point(2,2)
p3.update(2)
print(p1.counter)
print(p2.counter)
print(p3.counter)
print("--------------")
p3.counter = [0]
print(p1.counter)
print(p2.counter)
print(p3.counter)

## ZAD 5
print("******* ZAD 5 *******")

class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


jozek = Pracownik("Józek", "Bajka", 2000)
adrian = Menadzer("Adrian", "Mikulski", 12000)
adam = Osoba("Adam","Kowalski")

print(isinstance(adam,object))
print(isinstance(adrian,list))
print(issubclass(Pracownik,Osoba))
print(issubclass(Osoba,Pracownik))
print(issubclass(Menadzer,Osoba))

## ZAD 6
print("******* ZAD 6 *******")

tekst = "tekst"
it = iter(tekst)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

## ZAD 7
print("******* ZAD 7 *******")

class parzyste:
    def __init__(self, data):
        self.data = data
        self.index = 2
        self.length = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        self.index = self.index+2
        return self.data[self.index-2]
       

test = parzyste("wyImAgInOwAnY")
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))

## ZAD 8
print("******* ZAD 8 *******")

class samogloski:
    samogl = ['a','e','i','o','u','ó','y',"A","E","I","O","U","Ó","Y"]
    def __init__(self, data):
        if(type(data) != str):
            print("argument nie jest stringiem") 
        else:
            self.data = data
            self.index = 0
            self.length = len(data)
        
    def __iter__(self):
        return self
    def __next__(self):
        while self.data[self.index] not in self.samogl:
            self.index = self.index+1
        if(self.index == self.length):
            raise StopIteration
        self.index = self.index+1
        return self.data[self.index-1]


test = samogloski("testowankoIAO")
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))

## ZAD 9
print("******* ZAD 9 *******")

def parz(data):
    for index in range(2,len(data),2):
        yield data[index]

gen = parz("TESTOWANKO")
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

## ZAD 10
print("******* ZAD 10 *******")

def kombinacje():
    list = [1,2,3,4,5,6,7,8,9,10]
    for i in itertools.combinations(list,3):
        yield print(i)
test = kombinacje()

print(next(test))
print(next(test))
print(next(test))
print(next(test))

## ZAD 11
print("******* ZAD 11 *******")

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a

fibo = fib(10)
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))
print(next(fibo))

## ZAD 12
print("******* ZAD 12 *******")

def miesiace():
    miesiace =["Styczeń","Luty","Marzec","Kwiecień","Maj","Czerwiec","Lipiec","Sierpień","Wrzesień","Październik","Listopad","Grudzień"]
    for index in range(12):
        yield miesiace[index]

mies = miesiace()
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))









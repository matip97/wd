import numpy as np

# ZAD 1
lista = []
for i in range(100):
    if i%4==0:
        lista +=[i]
plik = open("zad1.txt","w+")
plik.writelines(str(lista))
plik.close()

# ZAD 2
plik = open("zad1.txt","r")
lista = plik.readline()
print(lista)
plik.close()

# ZAD 3
with open("zad3.txt","r") as plik:
    for linia in plik:
        print(linia,end="")

# ZAD 4 
print('\n')
class NaZakupy:
    nazwa_produktu =""
    ilosc = 0
    jednostka_miary = ""
    cena_jed =0
    def __init__(self,a,b,c,d):
        self.nazwa_produktu = a
        self.ilosc = b
        self.jednostka_miary = c
        self.cena_jed = d
    def wyswietl_produkt(self):
        return self.nazwa_produktu + " \nilość: " + str(self.ilosc) + " "+ self.jednostka_miary + " \ncena: " + str((self.cena_jed*self.ilosc))

    def ile_produktu(self):
        return str(self.ilosc) + " " + self.jednostka_miary
    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed
    

koszyk = NaZakupy("czekolada", 5,"szt",2.50)
print(koszyk.wyswietl_produkt())
print(koszyk.ile_produktu())
print(koszyk.ile_kosztuje())

# ZAD 5
print()
class CiagArytmetyczny:
    ciag=[]
    a=0
    def __init__(self,a0,r,ile):
        for x in range(ile):
            if x==0:
                self.a=a0
                self.ciag+=[self.a]
            else:
                self.a+=r
                self.ciag+=[self.a]
    def pobierz_element(self,x):
        x=x-1
        return self.ciag[x]
    def suma(self):
        suma =0
        for x in range(len(self.ciag)):
            suma += self.ciag[x]
        return suma
    def elementy(self):
        x = self.ciag.__len__()
        return x
    

nowy = CiagArytmetyczny(1,2,10)
print(nowy.ciag)
print(nowy.pobierz_element(2))
print(nowy.suma())
print(nowy.elementy())
       
# ZAD 6
print()
class Slowa:
    slowa = ["tata","mata","kajak","kake","tama"]

    def czy_palidrom(self,x):
        a = self.slowa[x-1]
        length = a.__len__()
        y=length-1
        for z in range(length):
            if a[z] != a[y]:
                return "nie pandolim"
            else:
                y-=1
        return "pandolim"

    def czy_metagramy(self,a,b):
        wyr1 = self.slowa[a-1]
        wyr2 = self.slowa[b-1]
        roznice =0
        len1 = wyr1.__len__()
        len2 = wyr2.__len__()
        if len1 != len2 :
            return "Sprawdzane wyrazy powinny być równej długości"
        for x in range(len1):
            if(wyr1[x] != wyr2[x]):
                roznice+=1
        if roznice ==0 :
            return "slowa identyczne"
        elif roznice == 1:
            return "metagram"
        else:
            return "słowa różne"

    def czy_anagram(self,a,b):
        wyr1 = self.slowa[a-1]
        wyr2 = self.slowa[b-1]
        litery = []
        for x in range(wyr1.__len__()):
            litery += [wyr1[x]]
        for x in range(wyr2.__len__()):
            if wyr2[x] not in litery:
                return "nie anagram"
        return "anagram"
    def wyswietl_wyrazy(self):
        for x in range(self.slowa.__len__()):
            print(self.slowa[x])
        return ""



gierka = Slowa()
print(gierka.czy_palidrom(3))
print(gierka.czy_metagramy(1,2))
print(gierka.czy_anagram(2,5))
print()
print(gierka.wyswietl_wyrazy())

# ZAD 7

class Robaczek:
    x=0
    y=0
    krok=0

    def __init__(self,x,y,krok):
        self.x = x
        self.y = y
        self.krok = krok
    
    def idz_w_gore(self,ile_kroków):
        self.y += self.krok*ile_kroków
    def idz_w_dol(self,ile_kroków):
        self.y -= self.krok*ile_kroków
    def idz_w_prawo(self,ile_kroków):
        self.x += self.krok*ile_kroków
    def idz_w_lewo(self,ile_kroków):
        self.x -= self.krok*ile_kroków
    def gdzie_jestem(self):
        return self.x , self.y
    def __del__(self):
        print("deleted")
    

pelzacz = Robaczek(0,0,1)
pelzacz.idz_w_gore(10)
pelzacz.idz_w_dol(2)
pelzacz.idz_w_prawo(50)
pelzacz.idz_w_lewo(10)
print(pelzacz.gdzie_jestem())

# ZAD 8 
print(pelzacz)
del pelzacz
print(pelzacz)


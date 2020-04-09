import numpy as np
import math
import sys
import zespolone.zespolone1 as z1
import zespolone.zespolone2 as z2
import ciagi.arytmetyczny as arytmetyczne
import ciagi.geometryczny as geometryczny
# ZAD 1
print("ZAD 1")
A=[1/x for x in range(1,10)]
print(A)
B=[2**n for n in range(10)]
print(B)
C=[x for x in B if x%4==0]
print(C)

# ZAD 2
print("\n ZAD 2")
macierz3x3 = np.array([np.random.randint(0,10, size=3),
np.random.randint(0,10, size=3), np.random.randint(0,10, size=3)])
print(macierz3x3)
lista1 = macierz3x3.diagonal()
print("Przekątna: ")
print(lista1)

# ZAD 3
print("\n ZAD 3")
listaProduktow = {
    "jajka" : "sztuki",
    "ziemniaki": "kilogramy",
    "mąka": "opakowania"
}
print(listaProduktow.items())

# ZAD 4
print("\n ZAD 4")
def monot(a=0):
    if a<0:
        print(f"funkcja malejaca dla a = {a}")
    if a>0:
        print(f"funkcja rosnaca dla a = {a}")
    if a==0:
        print(f"funkcja stała dla a = {a}")
monot(3)

# ZAD 5
print("\n ZAD 5")
def proste(a1=0, a2=0):
    if(a1==a2):
        print(f"Proste y={a1}x+b oraz y={a2}x+b są rówboległe")
    if(a1*a2 ==-1):
        print(f"Proste y={a1}x+b oraz y={a2}x+b są prostopadłe")
proste(2,-0.5)

# ZAD 6
print("\n ZAD 6")
def okrag(x=2,y=4):
    r=math.sqrt(x**2+y**2)
    return r
print(okrag())

# ZAD 7
print("\n ZAD 7")
def przeciwProstokatna(a=4,b=3):
    c = math.sqrt(a**2+b**2)
    return c
print(przeciwProstokatna())

# ZAD 8
print("\n ZAD 8")
def sumaCiagu(a1=1,r=1,ile=10):
    Ciag = []
    c=0
    suma =0
    for x in range(ile):
        if x==0:
            c=a1
            Ciag.append(c)
        else:
            c+=r
            Ciag.append(c)
    for x in range(ile):
        suma +=Ciag[x]
    return suma
#wiem że można było zorbić to krócej. Chciałem jednak przećwiczyć dodatkowo listy :)
print(sumaCiagu(1,2,5))

# ZAD 9
print("\n ZAD 9")
def iloczynCiagu(a1=1,r=1,ile=10):
    iloczyn = 1
    a=0
    for x in range(ile):
        if x==0:
            a=a1
            iloczyn*=a
        else:
            a+=r
            iloczyn*=a
    return iloczyn
print(iloczynCiagu())

# ZAD 10
print("\n ZAD 10")
def zakupy(** rzeczy):
    razem=0
    for cos in rzeczy:
        razem+=rzeczy[cos]
    return razem

print(zakupy(ziemniaki=5,olej=1,mleko=5))

# ZAD 11
print("\n ZAD 11")
print(z1.rzeczywista(1,2))
print(z2.dodawanie(2,4,1,1))

# ZAD 12
print("\n ZAD 12")
print(arytmetyczne.iloczyn())
print(geometryczny.suma())
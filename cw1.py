# [print(f"liczba: {x}") for x in range(5)]
print(len([print(f"liczba: {x}") for x in range(5)]))

slownik = {'imie': 'Adam', 'wiek': 25}

for cos, cos2 in slownik.items():
    print(cos, cos2)

slownik2 = {str(x):x for x in range(10)}
slownik2 = {wartosc: klucz for klucz, wartosc in slownik.items()}
print(slownik2)

#funkcje
def ciag(* liczby):
    if len(liczby)== 0:
        return 0.0
    else:
        suma =0.0

        for i in liczby:
            suma+= i
        return suma

print(ciag())
print(ciag(1,2,3,4,5))

def witaj(imie="janek"):
    """ return: None """
    print(f'Witaj {imie} !')
witaj()

short =  witaj #alias do funkcji
short('dawid')
print(short.__str__())
print(type(short))
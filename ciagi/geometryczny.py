def suma(a1=1,r=2,ile=5):
    suma = 0
    a=0
    for x in range(ile):
        if x==0:
            a=a1
            suma+=a
        else:
            a*=r
            suma+=a
    return suma
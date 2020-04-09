def iloczyn(a1=1,r=1,ile=10):
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
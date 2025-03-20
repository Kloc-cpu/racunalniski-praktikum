def razderli_na_pol_V1(mn):
    """
    Razdeli dobljeno množico na dve.
    """
    polovica = set()
    iteracija = set(mn)
    for el in mn:
        if len(iteracija) == len(polovica) or len(iteracija) == len(polovica) + 1:
            break
        polovica.add(el)
        iteracija.remove(el)
    return iteracija, polovica


def razdeli_na_pol_V2(mn):
    """
    Funkcija razdeli množico na dva dela
    """
    if len(mn) == 0:
        return {}
    if len(mn) == 1:
        return(mn,{})
    
    mn = list(mn)
    mnA = set()
    mnB = set()
    vel = len(mn)
    for el in range(vel//2):
        mnA.add(mn[el])
    for el in range(vel//2, vel):
        mnB.add(mn[el])
    

    return(mnA, mnB)


def razdeli_na_pol_V3(mn):
    """
    Vrne nabor dveh množic, katerih unija je enaka parametru mn.
    Vrne None, če parameter ni množica.
    """
    if type(mn) != set:
        return None
    
    A = set()
    B = set()
    
    for el in mn:
        if len(A) > len(B):
            B.add(el)
        else:
            A.add(el)

    return (A, B)













# Testni primeri

# Primer za prazno množico, preverimo: program se polomi ob prazni monžici
mnozica = {}
print("test case: {}\nfunc1:",razderli_na_pol_V1(mnozica),"\nfunc2:",razdeli_na_pol_V2(mnozica),"\nfunc3:",razdeli_na_pol_V3(mnozica))

# Primer tipične sode množice, preverimo: Splošno pravilno delovanje programa s sodimi množicami
mnozica = {3,2,5,1,4,7}
print("test case: {3,2,5,1,4,7}\nfunc1:",razderli_na_pol_V1(mnozica),"\nfunc2:",razdeli_na_pol_V2(mnozica),"\nfunc3:",razdeli_na_pol_V3(mnozica))

# Primer tipične lihe množice, preverimo: Splošno pravilno delovanje programa s lihimi množicami
mnozica = {1,2,3,4,5}
print("test case: {1,2,3,4,5}\nfunc1:",razderli_na_pol_V1(mnozica),"\nfunc2:",razdeli_na_pol_V2(mnozica),"\nfunc3:",razdeli_na_pol_V3(mnozica))

# Primer množice z enim elementom, preverimo: 2. del ozm množica 2 pravilno vrnjena, čeprav nima elementov
mnozica = {1}
print("test case: one element\nfunc1:",razderli_na_pol_V1(mnozica),"\nfunc2:",razdeli_na_pol_V2(mnozica),"\nfunc3:",razdeli_na_pol_V3(mnozica))





def razdelitev(tab, nakljucni_kamen):
    manjsi_od_kamna = []
    manjsi_so_sortirani = False
    vecji_od_kamna = []
    vecji_so_sortirani = False
    enaki = []
    kamenja = []
    

    for i in range(len(tab)):
        if(vsota_stevk(tab[i]) < vsota_stevk(tab[nakljucni_kamen])):
            manjsi_od_kamna.append(tab[i])
        elif(vsota_stevk(tab[i]) > vsota_stevk(tab[nakljucni_kamen])):
            vecji_od_kamna.append(tab[i])
        else:
            enaki.append(tab[i])
    enaki.append(tab[nakljucni_kamen])

    if(len(manjsi_od_kamna) == 2):
            manjsi_od_kamna = sortiranje_tabel_dolzine_2(manjsi_od_kamna)
            manjsi_so_sortirani = True
    elif(len(manjsi_od_kamna) == 1):
            manjsi_so_sortirani = True
    if(len(vecji_od_kamna) == 2):
            vecji_od_kamna = sortiranje_tabel_dolzine_2(vecji_od_kamna)
            vecji_so_sortirani = True
    elif(len(vecji_od_kamna) == 1):
            vecji_so_sortirani = True

    if(manjsi_so_sortirani and vecji_so_sortirani):
        manjsi_od_kamna += enaki
        manjsi_od_kamna += vecji_od_kamna
        return manjsi_od_kamna
    if(len(manjsi_od_kamna) > 1):
        kamenja += razdelitev(manjsi_od_kamna, random.randint(0,len(manjsi_od_kamna)-1))
    kamenja += enaki
    if(len(vecji_od_kamna) > 1):
        kamenja += razdelitev(vecji_od_kamna, random.randint(0,len(vecji_od_kamna)-1))

    return kamenja


def sortiranje_tabel_dolzine_2(tab):
     if(tab[0] > tab[1]):
                tab[0], tab[1] = tab[1], tab[0]
                return tab

    

def vsota_stevk(vrednost):
    """Izračuna vsoto števk in to vrednost vrne"""
    vrednost_vsote_stevk = 0
    while(vrednost != 0):
        vrednost_vsote_stevk += vrednost%10
        vrednost //= 10

    return vrednost_vsote_stevk

import random

tab = [1536616, 3462767, 42, 2162364, 410004544422, 3426547, 235747, 4444427, 25775]
nakljucni_kamen = random.randint(0,len(tab)-1)
print(razdelitev(tab, nakljucni_kamen))



#Testni primeri:
print(vsota_stevk(11))
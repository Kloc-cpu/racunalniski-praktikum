def razdelitev(tab, nakljucni_kamen):
    manjsi_od_kamna = []
    vecji_od_kamna = []
    enaki = []
    for i in range(len(tab)):
        if(tab[i] < tab[nakljucni_kamen]):
            manjsi_od_kamna.append(tab[i])
        elif(tab[i] > tab[nakljucni_kamen]):
            vecji_od_kamna.append(tab[i])
        else:
            enaki.append(tab[i])
    enaki.append(nakljucni_kamen)
    kamenja = []
    kamenja.append(manjsi_od_kamna)
    kamenja.append(enaki)
    kamenja.append(vecji_od_kamna)
    print(kamenja)

    if(kamenja == tab):
        return False
    else:
        return True

import random

tab = [1536616, 3462767, 42, 2162364, 410004544422, 3426547, 235747, 4444427, 25775]
nakljucni_kamen = random.randint(0,len(tab)-1)
razdelitev(tab, nakljucni_kamen)

x = True
for i in range(len(tab)):
    while(x):
        if not(razdelitev(tab[i],nakljucni_kamen)):
            x = False

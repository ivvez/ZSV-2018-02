'''
DNA je nukleinska kiselina koja sadrzi genetske upute za specificni
bioloski razvoj stanicnih oblika zivota. Izmedju dva DNA lanca postoje
ove kombinacije: A+T, T+A, C+G, G+C. Kazemo da su A i T te C i G komplementarni.

Napisi program koji ce za ucitani string znakova ispisati novi string koji
sadrzi komplementarne parove.

npr. ATTGC---->TAACG
'''

def dna_lanac(dna)
    s=''
    for i in dna:
    if i=='T':
        s+='A'
    elif i=='A':
        s+='T'
    elif i=='G':
        s+='C'
    elif i=='C':
        s+='G'

    return (dna)

#drugo rjesenje

def dna_lanac(dna):
    parovi = { "A":"T",
                  "T":"A",
                  "C":"G",
                  "G":"C"
                  }
    return "".join([parovi[x] for x in dna])


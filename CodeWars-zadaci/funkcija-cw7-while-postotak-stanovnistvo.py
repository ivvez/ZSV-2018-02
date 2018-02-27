'''
U malom gradu populacija je 1000 stanovnika na pocetku godine.
Populacija se povecava redovno 2% godisnje i jos 50 novih stanovnika dolazi
svake godine zivjeti u taj grad.
Napisi program koji ce izracunati koliko godina treba proci da populacija
bude veca ili jednaka p=1200 stanovnika za zadani postotak povecanja i
nove stanovnike.
'''

def godina(populacija, postotak, novi, p):
    godina = 0
    while populacija < p:
        populacija += populacija * postotak / 100. + novi
        godina += 1
    return godina

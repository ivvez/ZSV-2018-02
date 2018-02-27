#napisi program koji ce za zadani pocetni ton glazbene abecede sloziti 
#dur ili mol akord. Akord se sastoji od tri tona.
#dur: pocetni ton te 4 i 7 nakon njega
#mol: pocetni ton te 3 i 7 nakon njega

#glazbena abeceda: C, C#, D, D#, E, F, F#, G, G#, A, A#, B

note = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

a=input('Pocetni ton:')

n = note + note
i = n.index(a)
print( [[n[i], n[i+4], n[i+7]], [n[i], n[i+3], n[i+7]]])


#napisi funkciju koja za ucitanu listu imena vraca listu samo tvojih prijatelja
#tvoji prijatelji imaju iskljucivo 4 slova u imenu!

def prijatelj(x):
    nl=[]
    for i in x:
        if len(i)==4:
            nl.append(i)
    return nl


print(prijatelj(["Ivan", "Marko", "Tomislav","Luka" ]))

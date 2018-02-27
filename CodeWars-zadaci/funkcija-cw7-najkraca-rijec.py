#Napisi funkciju koja za ucitani string rijeci vraca najkracu rijec

def find_short(s):
    l=s.split()
    return len(min(l, key=len))

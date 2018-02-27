'''
Pero pastir ima jedan problem, svaki dan cuva ovce, ali nikako ne moze prebrojati
koliko ih ima. Pomozi mu izradom aplikacije koja ce to uciniti umjesto njega.
Napisi funkciju koja prima listu vrijednosti True ili False (True znaci
da je ovca prisutna, False da nije) i vraca ukupan broj ovaca.

Npr.
ar=[True,True,False,True,True,False] ----> Ukupno ima 4 ovce.
'''


def ovce(ar):
  c=0
  for i in ar:
      if i==True:
          c+=1
          
  return c


#rjesenje u jednom retku

def ovce(ar):
    return ovce.count(True)

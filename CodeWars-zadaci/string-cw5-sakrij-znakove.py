'''
Prilikom kupovine preko interneta, kada unosimo npr. broj kreditne kartice ili
broj telefona, dio broja se "maskira" tako da se zamijeni znakom #, a prikazu
se samo zadnje cetiri znamenke.

Napisi program koji ce za upisani niz znakova sakriti znakove na takav
nacin da ce sve znakove prekriti znakom #, osim zadnja cetiri!

Npr.

s=12567832423 ---> #######2423
s=567abcd98at ---> #######98at
'''

s=input()
print ("#"*(len(s)-4) + s[-4:])

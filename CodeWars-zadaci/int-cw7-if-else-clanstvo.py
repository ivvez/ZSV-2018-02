'''Teniski klub Osijek odlucio je 2017.god. uvesti dvije kategorije clanstva:
Otvoreno i Seniori.
Trebaju tvoju pomoc za izradu aplikacije koja ce postojece clanove kluba razvrstavati
u kategorije prema pravilima:
-ako je clan od 1.1.2017. stariji od 55 godina i clan je kluba vise od 3 godine bit ce u
kategoriji Senior
-ako je clan izmedju 12-55 godina bit ce u kategoriji Otvoreno.
Clanovi mladji od 12 godina za sada se nece svrstavati u kategorije te u njihovom
slucaju aplikacija treba ispisati znak '-' .

Ulazni podaci: godina rodjenja i vrijeme clanstva u klubu izrazeno u broju godina

'''

godiste=int(input())
clanstvo=int(input())

if 2017-godiste>55 and clanstvo>3:
    print ('Seniori')
elif 2017-godiste<=55 and 2017-godiste>=12:
    print ('Otvoreno')
else:
    print ('-')

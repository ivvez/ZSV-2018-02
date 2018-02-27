'''
napisi program koji unutar stringa ucitava niz brojeva odvojenih razmakom
te ispisuje najmanji i najveci od tih brojeva.
'''

def naj(brojevi):
  n = map(int, brojevi.split(' '))
  return "{} {}".format(max(n), min(n))

'''Napisi program koji za ucitano prvo slovo a i drugo slovo b ispisuje
sva slova abecednim redom koja se nalaze izmedju a i b.
Slova se trebaju ispisati u jednom retku.
'''

a=input()
b=input()
br=ord(a)
while br <= ord(b):
    print(chr(br), end=" ")
    br += 1

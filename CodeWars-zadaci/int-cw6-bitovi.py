#napisi program koji unosi cijeli broj n
#te ispisuje koliko taj broj u binarnom obliku ima jedinica

n=int(input())
print  (str(bin(n)).count('1'))

n=int(input())
s = 0
while n:
    s += n % 10
    n //= 10
print (s)

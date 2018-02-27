#Napisi program koji ce od n ucitanih prirodnih brojeva zbrojiti samo pozitivne

n=int(input())
z=0
for i in range(n):
    b=int(input())
    if b>0:
        z+=b

print (z)
    

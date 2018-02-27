#Napisi program koji ce ucitani niz brojeva ispisati od najmanjeg do najveceg

a=int(input())
nums=[]
for i in range(a):
    b=int(input())
    nums.append(b)
    
print (sorted(nums))

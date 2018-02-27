#napisi program koji unosi neki broj n te puni listu brojevima od 1-n
#program treba ispisati listu brojeva 1-n te obrnutu listu brojeva od n-1
#npr. n=5, [1,2,3,4,5] ---> [5,4,3,2,1]

n=int(input())
l=[]
for i in range(1,n+1):
    l.append(i)
print (l)
l.reverse()
print (l)

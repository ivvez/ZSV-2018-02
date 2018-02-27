'''
napisi program koji unosi listu brojeva i znakova te ispisuje novu listu
koja sadrzi samo brojeve
'''

a = [x for x in input().split()]

filt = []
for i in a:
    try:
        val=int(i)
        filt.append(i)
    except:
        pass

print(filt)

    

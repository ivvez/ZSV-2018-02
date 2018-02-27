'''
napisi program koji unosi neki broj te sortira njegove znamenke silazno,
od najvece do najmanje
'''

broj=int(input())
sort="".join(sorted(str(broj), reverse=True))
print (sort)

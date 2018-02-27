'''
napisi program tako da ispise rjesenje kao u primjerima ispod:

abcd -------> A-Bb-Ccc-Dddd
RqaEzty ----> R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy
cwAt -----  > C-Ww-Aaa-Tttt

'''

s=input()
br=1
s2=''
for i in s:
    s2+=(i*br)+'-'
    br+=1
    
print (s2.title()[:-1])

# rjesenje u jednom retku:

def duplaj(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

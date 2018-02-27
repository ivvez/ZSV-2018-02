#napisi program koji ce iz ucitanog stringa izbaciti sve samoglasnike

string=input()
ns=''
string2=''
for x in string:
    if x in 'aeiouAEIOU':
        ns = ns.replace(x, "")
        string2=string2+ns
    else:
        string2=string2+x
print (string2)


'''
rjesenje u jednom retku:
def izbaci(s):
    return s.translate(None, "aeiouAEIOU")
'''

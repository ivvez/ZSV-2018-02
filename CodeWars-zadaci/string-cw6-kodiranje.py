'''Napisi program koji ce ucitani string kodirati tako da znak koji se
u ucitanom stringu ponavlja samo jednom zamijenis s "(", a ako se znak ponavlja
vise puta zamijeni ga sa "(".

Npr.
"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

'''

s1=input()
s1=s1.lower()
s2=''
for i in s1:
    if s1.count(i)==1:
        s2+='('
    else:
        s2+=')'

print (s2)

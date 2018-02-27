'''
za ucitani broj n ispisi novi broj m koji ce sadrzavati kvadrate svake znamenke
broja n
npr.
n=9119 ------> m=811181  

'''

def square_digits(num):
    k=''
    for i in str(num):
        k+=str(int(i)**2)
    return int(k)

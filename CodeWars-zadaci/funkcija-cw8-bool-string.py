'''
Napisi funkciju koja prima bool vrijednost True ili False te vraca tekst
'Yes' ili 'No' ovisno o ucitanoj bool vrijednosti.
'''

def bool_to_word(bool):
    if bool==True:
        return 'Yes'
    else:
        return 'No'

#rjesenje u jednom retku
    
def bool_to_word(bool):
    return "Yes" if bool else "No"

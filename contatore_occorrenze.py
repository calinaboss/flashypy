lista = ['a', 'b', 'a', 'c', 'b', 'a']
conteggio = {}
for el in lista:
    conteggio[el] = conteggio.get(el, 0) + 1
print(conteggio)

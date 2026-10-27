try:
    with open('dati.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('file non trovato')

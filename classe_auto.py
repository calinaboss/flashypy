class Auto:
    def __init__(self, marca, velocita=0):
        self.marca = marca
        self.velocita = velocita
    def accelera(self):
        self.velocita += 10

a = Auto('Fiat')
a.accelera()
print(a.velocita)

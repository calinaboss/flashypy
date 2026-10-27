class Auto:
    def __init__(self, marca, velocita=0):
        self.marca = marca
        self.velocita = velocita
    def accelera(self):
        self.velocita += 10
    def frena(self):
        self.velocita -= 5

a = Auto('Fiat')
a.accelera()
a.frena()
print(a.velocita)

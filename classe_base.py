class Persona:
    def __init__(self, nome):
        self.nome = nome
    def saluta(self):
        print('ciao sono', self.nome)

p = Persona('Luca')
p.saluta()

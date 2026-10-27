class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    def saluta(self):
        print('ciao sono', self.nome, 'e ho', self.eta, 'anni')

p = Persona('Luca', 22)
p.saluta()

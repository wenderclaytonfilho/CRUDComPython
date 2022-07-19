
class Contato():
    def __init__(self, tipo, dado):
        self.tipo = tipo
        self.dado = dado
    def __str__(self):
        return '{} - {}'.format(self.tipo, self.dado)


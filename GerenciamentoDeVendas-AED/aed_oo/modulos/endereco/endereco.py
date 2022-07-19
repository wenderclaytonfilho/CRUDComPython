class Endereco():
    def __init__(self,cep,numeroDaCasa,estado):
        self.cep = cep
        self.numeroDaCasa = numeroDaCasa
        self.estado = estado
        self.rua = None
        self.bairro = None
        self.cidade = None
        

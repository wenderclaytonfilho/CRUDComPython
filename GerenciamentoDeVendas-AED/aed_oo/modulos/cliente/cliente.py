from modulos.contato.contato import Contato
class Cliente():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.endereco = None
        self.__contatos = []
        self.contato = Contato
    def __str__(self):
        return '{}-{}'.format(self.nome, self.cpf)

    def validar_contato(self, contato):
        if contato.tipo != "facebook" or contato.tipo != "email" or contato.tipo != "fone" or contato.tipo != "instagram":
            print("Contato de tipo válido, será adicionado ao cliente!")
            return contato
        else:
            print("Contato de tipo inválido! Use apenas: facebook,instagram,fone ou email")

    def add_contato(self, contato):
        contatoValido = self.validar_contato(contato)
        self.__contatos.append(contatoValido)

    def lista_contatos(self):
        return self.__contatos.copy()




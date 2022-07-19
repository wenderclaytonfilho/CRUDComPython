from modulos.endereco.endereco import Endereco

class DaoCliente():
    def __init__(self):
        self.__clientes = []

    def salvar_cliente(self, cliente):
        if self.buscar_cliente(cliente.cpf) is None:
            self.__clientes.append(cliente)
            return True
        return False

    def buscar_cliente(self, cpf):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def adicionar_endereco(self, cliente):
        print("Adicionado o endereco ao cliente = {}".format(cliente.nome))
        cep = input("Digite o CEP: ")
        numeroDaCasa = input("Digite o numero da casa: ")
        estado = input("Digite o estado (APENAS A SIGLA, EX: PERNAMBUCO = PE: ").upper()
        cliente.endereco = Endereco(cep, numeroDaCasa, estado)
        print("Endereço adicionado com sucesso!")

    def lista_clientes(self):
        return self.__clientes.copy()
from modulos.cliente.cliente import Cliente
from modulos.cliente.dao_cliente import DaoCliente
from modulos.contato.contato import Contato

class ControladorCliente():
    def __init__(self):
        self.__dao = DaoCliente()
        self.clienteClasse = Cliente
        self.contato = Contato
    def menu(self):
        print('--------')
        print('1 - Novo Cliente')
        print('2 - buscar por CPF')
        print('3 - listar clientes')
        print('4 - Listar clientes por Estado')
        print('5 - adicionar contato à um Cliente')
        print('6 - adicionar endereço à um Cliente')
        print('0 - SAIR')

    def cadastra_cliente(self):
        print('--=Cadastro de Cliente=--')
        nome = input("Digite o Nome :> ")
        cpf = input("Digite o CPF:> ")
        while True:
            escolha = input("-O cliente será salvo no banco de dados, deseja adicionar endereço?\n1-SIM\n2-NÃO\n")
            if escolha == "1":
                self.__dao.salvar_cliente(Cliente(nome, cpf))
                cliente = self.__dao.buscar_cliente(cpf)
                self.__dao.adicionar_endereco(cliente)
                print("Cliente adicionado com sucesso!")
                break
            if escolha == "2":
                if self.__dao.salvar_cliente(Cliente(nome, cpf)):
                    print('Adicionado com Sucesso')
                    break
                else:
                    print('CPF já existente')
                    break
            else:
                print("Opção inválida!")

    def adicionar_endereco_a_um_cliente(self):
        print("--=Adicionar endereço à um cliente=--")
        cpf = input("Digite o cpf do cliente:> ")
        cliente = self.__dao.buscar_cliente(cpf)
        self.__dao.adicionar_endereco(cliente)


    def buscar_cliente(self):
        print("--=Buscar cliente por CPF=--")
        cpf = input("Digite o cpf do cliente que deseja buscar")
        cliente =self.__dao.buscar_cliente(cpf)
        if cliente is None:
            print("Cliente inexistente")
        else:
            print("{} - {} - {}".format(cliente.nome,cliente.cpf,cliente.endereco.estado))

    def listar_clientes(self):
        print("--=Lista de Clientes=--")
        clientes = self.__dao.lista_clientes()
        for cliente in clientes:
            if cliente.endereco == None:
                print("{} - {} ".format(cliente.nome, cliente.cpf))
            else:
                print("{} - {} - {}".format(cliente.nome,cliente.cpf,cliente.endereco.estado))
        if len(clientes) == 0:
            print("A lista de clientes está vazia!")

    def listar_clientes_por_estado(self):
        print("--=Lista de clientes por estado=--")
        filtro = input("Digite o estado que deseja filtrar:> ").upper()
        clientes = self.__dao.lista_clientes()
        print("--=Clientes de {}=--".format(filtro))
        for cliente in clientes:
            if cliente.endereco == None:
                pass
            else:
                if cliente.endereco.estado == filtro:
                    print("{} - {} - {}".format(cliente.nome,cliente.cpf,cliente.endereco.estado))

    def adicionar_contato_a_um_cliente(self):
        print("--=Adicionar contato à um cliente=--")
        cpf = input("Digite o CPF do cliente que deseja buscar para adicionar um contato:> ")
        cliente =self.__dao.buscar_cliente(cpf)
        if cliente == None:
            print("Cliente Inexistente! ")
        else:
            dado = input("Digite o dado do contato: ")
            tipo = input("Digite o tipo do contato (facebook,instagram,fone ou email):> ").lower()
            Cliente.add_contato(cliente,Contato(tipo,dado))
            print(Contato(tipo,dado))
            print("Contato adicionado com sucesso!")


    def _get_cliente(self,cpf):
        return self.__dao.buscar_cliente(cpf)

    def iniciar_sistema(self):
        while True:
            self.menu()
            op = input("Digite a opção: ")
            if op == '1':
                self.cadastra_cliente()
            elif op =='2':
                self.buscar_cliente()
            elif op == '3':
                self.listar_clientes()
            elif op == "4":
                self.listar_clientes_por_estado()
            elif op == "5":
                self.adicionar_contato_a_um_cliente()
            elif op =="6":
                self.adicionar_endereco_a_um_cliente()
            elif op =='0':
                input('Saindo do módulo de cliente - Digite Enter')
                return
            else:
                print('Opção inválida, tente novamente')



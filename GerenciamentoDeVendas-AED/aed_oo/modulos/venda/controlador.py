from modulos.cliente.controlador import ControladorCliente
from modulos.produto.controlador import ControladorProduto
from modulos.venda.dao_venda import DaoVenda
from modulos.venda.venda import Venda
class ControladorVenda():
    def __init__(self,controlador_cliente:ControladorCliente ,controlador_produto:ControladorProduto):
        self.__dao = DaoVenda()
        self.controlador_produto = controlador_produto
        self.controlador_cliente =controlador_cliente


    def menu(self):
        print('--------')
        print('1 - Nova venda')
        print('2 - Buscar venda por código')
        print('3 - Listar todas as vendas')
        print('4 - Listar vendas por Cliente')
        print('5 - Listar Todas as vendas por Estado')
        print('6 - Quantas vendas tem no sistema')
        print('7 - Total de produtos vendidos')
        print('8 - Listar valor total de todas as vendas')
        print('0 - SAIR')

    def nova_venda(self):
        print("--=Criar nova venda=--")

        cpf = input("Digite o CPF do cliente, para criar uma nova venda:> ")
        cliente = self.controlador_cliente._get_cliente(cpf)
        if cliente is not None:
            listaProdutos = []
            listaProdutosExistentes = self.controlador_produto._get_lista_de_produtos()
            print("Cliente encontrado!\n{} - {}".format(cliente.nome,cliente.cpf))
            codigoDaVenda = input("Digite o código da venda que irá ser criada:> ")
            venda = self.__dao.buscar_venda(codigoDaVenda)
            if venda is not None:
                print("Código de venda já existente! Tente novamente com um outro código!")
            else:
                while True:
                    opcao = input("Deseja adicionar um produto na lista?\n1 - SIM\n0 - NÃO")
                    if opcao == "1":
                        print(self.controlador_produto._get_listar_produtos())
                        codigoProduto = input("Digite o código do produto que deseja adicionar na lista de produtos da venda:> ")
                        produtoExistente = 0
                        for produto in listaProdutosExistentes:
                            if produto.codigo == codigoProduto:
                                listaProdutos.append(produto)
                                produtoExistente+=1
                        if produtoExistente == 0:
                            print("O código do produto digitado não existe, portanto não será adicionado!! ")

                    if opcao == "0":
                        if len(listaProdutos) == 0:
                            print("É necesário ter pelo menos 1 produto para realizar uma venda! ")
                        else:
                            venda = Venda(codigoDaVenda, cliente)
                            venda.adicionar_produtos_na_venda(listaProdutos)
                            self.__dao.salvar_venda(venda)

                            #Imprimindo a venda finalizada
                            print("{} - {} ".format(venda.codigo,venda.cliente.nome))
                            i = 0
                            while i<len(listaProdutos):
                                print("{} - {} - {}".format(listaProdutos[i].codigo,listaProdutos[i].descricao, listaProdutos[i].valor))
                                print("-"*20)
                                i+=1
                            print("Venda salva com sucesso")
                            break
                    elif(opcao!="1" and opcao!="0"):
                        print("Opção inválida!")
        else:
            print("Cliente inexistente!!")

    def buscar_venda_por_codigo(self):
        print("--=Buscar venda por código=--")
        codigo = input("Digite o codigo da venda que deseja buscar: ")
        venda = self.__dao.buscar_venda(codigo)
        if venda is not None:
            print("--=VENDA {}=--".format(codigo))

            print("Cliente: {}\nCPF: {}\nCódigo: {}".format(venda.cliente.nome,venda.cliente.cpf,venda.codigo))
            print("--=PRODUTOS=--")
            for produto in venda.lista_de_produtos():
                print("Código: {} - Descrição: {} - Valor: {} ".format(produto.codigo,
                                                                       produto.descricao,
                                                                       produto.valor))
            print("-" * 20)
        else:
            print("Venda inexistente!")

    def listar_todas_as_vendas(self):
        print("--=Listar todas as vendas=--")
        for venda in self.__dao.lista_vendas():
            print("-" * 20)
            print("Cliente: {}\nCPF: {}\nCódigo da venda: {}".format(venda.cliente.nome, venda.cliente.cpf, venda.codigo))
            print("--=PRODUTOS=--")
            for produto in venda.lista_de_produtos():
                print("Código: {} - Descrição: {} - Valor: {} ".format(produto.codigo,
                                                                       produto.descricao,
                                                                       produto.valor))
            print("-"*20)


    def listar_vendas_por_cliente(self):
        print("--=Listar vendas por cliente=--")
        i = 0
        cpf = input("Digite o CPF do cliente que deseja buscar as vendas")
        cliente = self.controlador_cliente._get_cliente(cpf)
        for venda in self.__dao.lista_vendas():
            if venda.cliente.cpf == cliente.cpf:

                print("Cliente: {}\nCPF: {}\nCódigo: {}".format(venda.cliente.nome,venda.cliente.cpf,venda.codigo))
                print("--=PRODUTOS=--")
                for produto in venda.lista_de_produtos():
                    print("Código: {} - Descrição: {} - Valor: {} ".format(produto.codigo,
                                                                           produto.descricao,
                                                                           produto.valor))
                print("-" * 20)


    def listar_todas_as_vendas_por_estado(self):
        i = 0
        filtro = input("Digite o estado que deseja filtrar na busca de vendas:> ").upper()
        for venda in self.__dao.lista_vendas():
            if venda.cliente.endereco is not None:
                if venda.cliente.endereco.estado == filtro:

                    print("Cliente: {}\nCPF: {}\nCódigo: {}".format(venda.cliente.nome,venda.cliente.cpf,venda.codigo))
                    print("--=PRODUTOS=--")
                    for produto in venda.lista_de_produtos():
                        print("Código: {} - Descrição: {} - Valor: {} ".format(produto.codigo,
                                                                               produto.descricao,
                                                                               produto.valor))
                    print("-" * 20)


    def quantas_vendas_tem_o_sistema(self):
        print("--=Quantas vendas tem no sistema=--")
        if len(self.__dao.lista_vendas()) == 0:
            print("Não existem vendas no sistema!")
        else:
            print("O sistema tem: {} vendas.".format(len(self.__dao.lista_vendas())))

    def total_de_produtos_vendidos(self):
        print("--=Total de produtos vendidos=--")
        produtosAnt = 0
        produtos = 0
        i = 0
        while True:
            for venda in self.__dao.lista_vendas():
                listaDeProdutos = venda.lista_de_produtos()
                produtosSoma = len(listaDeProdutos)
                produtos = produtosAnt+ produtosSoma
                produtosAnt = produtosSoma
            print("Total de produtos vendidos = {}".format(produtos))
            break
    def listar_valor_total_de_todas_as_vendas(self):
        print("--=Listar valor total de todas as vendas=--")
        while True:
            for venda in self.__dao.lista_vendas():
                valores = []
                for valoresprodutos in venda.lista_de_produtos():
                    valorproduto = valoresprodutos.valor
                    valores.append(valorproduto)
                print("Venda {} - Total =R$ {}0".format(venda.codigo, sum(valores)))
                print("-" * 20)
            break


    def iniciar_sistema(self):
        while True:
            self.menu()
            op = input("Digite a opção: ")
            if op == '1':
                self.nova_venda()
            elif op =='2':
                self.buscar_venda_por_codigo()
            elif op == '3':
                self.listar_todas_as_vendas()
            elif op == "4":
                self.listar_vendas_por_cliente()
            elif op == "5":
                self.listar_todas_as_vendas_por_estado()
            elif op == "6":
                self.quantas_vendas_tem_o_sistema()
            elif op == "7":
                self.total_de_produtos_vendidos()
            elif op =="8":
                self.listar_valor_total_de_todas_as_vendas()
            elif op =='0':
                input('Saindo do módulo de Vendas - Digite Enter')
                return
            else:
                print('Opção inválida, tente novamente')




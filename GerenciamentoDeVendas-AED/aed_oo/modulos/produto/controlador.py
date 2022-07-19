from modulos.produto.dao_produto import DaoProduto
from modulos.produto.produto import Produto

class ControladorProduto():
    def __init__(self):
        self.__dao = DaoProduto()

    def menu(self):
        print('--------')
        print('1 - Cadastrar novo produto')
        print("2 - Buscar produto por código")
        print("3 - Listar todos os produtos")
        print('0 - SAIR')

    def cadastrar_produto(self):
        print('--=Cadastro de Produto=--')
        codigo = input("Digite o Código do produto :> ")
        descricao = input("Digite a descrição do produto:> ")
        valor = float(input("Digite o valor do produto:> "))
        if self.__dao.salvar_produto(Produto(codigo,descricao,valor)):
            print('Adicionado com Sucesso')
        else:
            print('Código já existente')

    def _get_buscar_produto(self):
        return self.buscar_produto()

    def buscar_produto(self):
        print("--=Buscar produto por código=--")
        codigo = input("Digite o código do produto:> ")
        produto =self.__dao.buscar_por_codigo(codigo)
        if produto is None:
            print("Produto inexistente")
        else:
            print('Código - {}\nDescrição - {}\nValor - R$ {}0'.format(produto.codigo, produto.descricao, produto.valor))

    def _get_listar_produtos(self):
        return self.__dao.listar_todos_os_produtos()

    def _get_lista_de_produtos(self):
        return self.__dao.lista_produtos()

    def iniciar_sistema(self):
        while True:
            self.menu()
            op = input("Digite a opção: ")
            if op == '1':
                self.cadastrar_produto()
            elif op =='2':
                self.buscar_produto()
            elif op == '3':
                self.__dao.listar_todos_os_produtos()
            elif op =='0':
                input('Saindo do módulo de produto - Digite Enter')
                return
            else:
                print('Opção inválida, tente novamente')
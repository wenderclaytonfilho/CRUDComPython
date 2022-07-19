class DaoProduto():
    def __init__(self):
        self.__produto = []

    def salvar_produto(self,produto):
        if self.buscar_por_codigo(produto.codigo) is None:
            self.__produto.append(produto)
            return True
        return False
    def lista_produtos(self):
        return self.__produto.copy()

    def buscar_por_codigo(self, codigo):
        for produto in self.__produto:
            if produto.codigo == codigo:
                return produto
        return None

    def listar_todos_os_produtos(self):
        for produto in self.__produto:
            print('Código - {}\nDescrição - {}\nValor - R$ {}0'.format(produto.codigo,produto.descricao,produto.valor))
            print('------')

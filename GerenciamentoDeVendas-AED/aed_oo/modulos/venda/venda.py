class Venda():
    def __init__(self,codigo,cliente):
        self.codigo = codigo
        self.cliente = cliente
        self.__listaDeProdutos = []

    def __str__(self):
        return ("Código - {}\nCliente - {}\nProdutos - {}".format(self.codigo,self.cliente,self.__listaDeProdutos))

    def total_da_venda(self):
        soma = []
        for i in self.__listaDeProdutos:
            soma.append(i.valor)
        return sum(soma)

    def lista_de_produtos(self):
        return self.__listaDeProdutos.copy()

    def adicionar_produtos_na_venda(self,listaProdutos):
        self.__listaDeProdutos = listaProdutos




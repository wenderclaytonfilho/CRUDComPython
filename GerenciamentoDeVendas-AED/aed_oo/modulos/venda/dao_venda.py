
class DaoVenda():
    def __init__(self):
        self.__vendas = []

    def salvar_venda(self, venda):
        if self.buscar_venda(venda.codigo) is None:
            self.__vendas.append(venda)
            return True
        return False

    def buscar_venda(self,codigo):
        for venda in self.__vendas:
            if venda.codigo == codigo:
                return venda
        return None


    def lista_vendas(self):
        return self.__vendas.copy()


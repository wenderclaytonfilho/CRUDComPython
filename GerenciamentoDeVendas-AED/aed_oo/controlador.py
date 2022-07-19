from modulos.cliente.controlador import ControladorCliente
from modulos.produto.controlador import ControladorProduto
from modulos.venda.controlador import ControladorVenda
class Sistema():
    def __init__(self):
        self.__controlador_cliente = ControladorCliente()
        self.__controlador_produto = ControladorProduto()
        #Passar o "dao" por meio do controlador para evitar a busca diretado DAO já que ele é privado
        self.__controlador_venda = ControladorVenda(self.__controlador_cliente,self.__controlador_produto)
    def menu_principal(self):
        print('--------')
        print('1 - Cliente')
        print('2 - Produto')
        print('3 - Venda')
        print('0 - SAIR')

    def iniciar(self):
        while True:
            self.menu_principal()
            op = input("Digite a opção: ")
            if op == '1':
                self.__controlador_cliente.iniciar_sistema()
            elif op =='2':
                self.__controlador_produto.iniciar_sistema()
            elif op == '3':
                self.__controlador_venda.iniciar_sistema()
            elif op =='0':
                input('Saindo do sistema - Digite Enter')
                return
            else:
                print('Opção inválida, tente novamente')

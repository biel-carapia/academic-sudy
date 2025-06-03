class Cartao():

    def __init__(self):
        self._limite = 100

    def _alterar_limite(self, novo_limite):
        if novo_limite < 0:
            raise ValueError('O limite não pode ser negativo!')
        else:
            self._limite = novo_limite

    def _exibir_limite(self):
        return self._limite

    limite = property(_exibir_limite, _alterar_limite)



cartao = Cartao()
cartao.limite = -150
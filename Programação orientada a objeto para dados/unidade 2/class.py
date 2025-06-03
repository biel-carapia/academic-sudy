class Carteira(): 

    saldo = 0

    def adicionar_fundos(self, valor):
        self.saldo += valor
        print('Operação realizada com sucesso!')

    def remover_fundos(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print('Operação realizada com sucesso!')
        else:
            print('Operação não realizada. Saldo insuficiente')

    def exibir_saldo(self):
        print('Seu saldo é de {self.saldo}')


#Testando diferentes carteiras
carteira_1 = Carteira()
carteira_1.adicionar_fundos(10)
carteira_1.exibir_saldo()


carteira_2 = Carteira()
carteira_2.adicionar_fundos(20)
carteira_2.exibir_saldo()

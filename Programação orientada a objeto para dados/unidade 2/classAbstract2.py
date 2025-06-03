from abc import ABC, abstractmethod

 

class Conta(ABC):
    def __init__(self, numero_da_conta, saldo):
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        raise NotImplementedError
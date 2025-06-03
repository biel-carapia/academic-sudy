from abc import ABC, abstractmethod

class CartaoBase(ABC):
    @abstractmethod
    def calcular_cach_back(self, valor):
            pass
    

class CartaoGold(CartaoBase):
    def calcular_cash_back(self, valor):
        return valor * 0.03

       

class CartaoPlatinum(CartaoBase):
    def calcular_cash_back(self, valor):
        return valor * 0.05

       

class CartaoDiamond(CartaoBase):
    def calcular_cash_back(self, valor):
        return valor * 0.08
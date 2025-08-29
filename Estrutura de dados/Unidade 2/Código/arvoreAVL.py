class NoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir_recursivo(valor, self.raiz)

    def _inserir_recursivo(self, valor, no):
        if not no:
            return NoAVL(valor)
        
        if valor < no.valor:
            no.esquerda = self._inserir_recursivo(valor, no.esquerda)
        else:
            no.direita = self._inserir_recursivo(valor, no.direita)
        
        no.altura = max(self._obter_altura(no.esquerda), self._obter_altura(no.direita)) + 1
        fator_balanceamento = self._obter_fator_balanceamento(no)

        if fator_balanceamento > 1:
            if valor < no.esquerda.valor:
                return self._rotacao_esquerda(no)
            else:
                return self._rotacao_esquerda_direita(no)
        
        if fator_balanceamento < -1:
            if valor > no.direita.valor:
                return self.rotacao_esquerda(no)
            else:
                return self._rotacao_direita_esquerda(no)
            
        return no
    
    def _obter_altura(self, no):
        if not no:
            return 0
        return no.altura
    
    def _obter_fator_balanceamento(self, no):
        if not no:
            return 0
        return self._obter_altura(no.esquerda) - self._obter_altura(no.direita)

    def _rotacao_direita(self, no):
        filho_esquerda = no.esquerda
        neto_direita = filho_esquerda.direita

        filho_esquerda.direita = no
        no.esquerda = neto_direita

        no.altura = max(self._obter_altura(no.esquerda), self._obter_altura(no.direita)) + 1
        filho_esquerda.altura = max(self._obter_altura(filho_esquerda.esquerda), self._obter_altura(filho_esquerda.direita)) + 1

        return filho_esquerda
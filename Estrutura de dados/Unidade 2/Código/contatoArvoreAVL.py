class Contato: 
    def __init__(self, id, nome, telefone): 
        self.id = id 
        self.nome = nome 
        self.telefone = telefone 

    def __str__(self):
        return f"{self.id}, Nome:{self.nome}, Telefone:{self.telefone}"
    
class NodoAVL:
    def __init__(self, contato):
        self.contato = contato
        self.altura = 1
        self.esquerdo = None
        self.direito = None

    # Métodos para inserção, remoção, busca, cálculo de altura e balanceamento aqui. 

class AgendaAVL: 
    def __init__(self): 
        self.raiz = None 
 
    # Método para adicionar contatos 
    def adicionar(self, contato): 
        self.raiz = self._adicionar(self.raiz, contato) 

    def _adicionar(self, nodo, contato): 
        if not nodo: 
            return NodoAVL(contato) 
        elif contato.id < nodo.contato.id: 
            nodo.esquerdo = self._adicionar(nodo.esquerdo, contato) 
        else: 
            nodo.direito = self._adicionar(nodo.direito, contato)

    # Atualizar altura, verificar balanceamento e aplicar rotações se necessário. 
        return nodo 
  

  # Métodos para remoção e busca seriam implementados de forma similar, focando no balanceamento da árvore
class Node: 
    def __init__(self, value): 
        self.value = value 
        self.children = [] 

    def add_child(self, child_node): 
        self.children.append(child_node) 

    def get_children(self): 
        return self.children 
    
    def obter_idade_minima(faixa_etaria): 
        # Implementar a lógica para extrair a idade mínima da string da faixa etária 
        idade_minima = ""
        return idade_minima
    
    def recomendar_filmes(raiz, idade_usuario): 
        recomendacoes = [] 
        for faixa in raiz.get_children(): 
            if idade_usuario >= obter_idade_minima(faixa.value): 
                for filme in faixa.get_children(): 
                    recomendacoes.append(filme.value) 
        return recomendacoes
    

root = Node() 
livre = Node() 
dez_anos = Node() 
doze_anos = Node() 

# Adicionar outros nós para as faixas de 14, 16 e 18 anos 
root.add_child(livre) 
root.add_child(dez_anos) 
root.add_child(doze_anos) 

# Adicionar os demais nós de faixa etária à raiz 

# Adicionar filmes a cada nó de faixa etária 
livre.add_child(Node()) 
livre.add_child(Node()) 
livre.add_child(Node()) 

dez_anos.add_child(Node()) 
dez_anos.add_child(Node()) 
dez_anos.add_child(Node()) 

doze_anos.add_child(Node()) 
doze_anos.add_child(Node()) 
doze_anos.add_child(Node()) 

# Continuar adicionando filmes para as demais faixas etárias

print(recomendar_filmes(root, 20)) # Deverá retornar filmes de todas as faixas 

print(recomendar_filmes(root, 13)) # Deverá retornar filmes até a faixa de 12+ 
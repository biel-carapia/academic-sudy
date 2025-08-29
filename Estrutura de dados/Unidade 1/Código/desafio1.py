# Você foi apresentado à seguinte problemática:

# Você é um programador trabalhando em um sistema de gestão de bibliotecas e 
# precisa desenvolver uma funcionalidade que armazene e gerencie informações 
# sobre os livros e os empréstimos. Como você poderia construir uma solução em 
# Python para tal?

# Para armazenar informações sobre os livros, você pode utilizar um dicionário built-in 
# em Python, pois ele permite armazenar pares de chave-valor, facilitando a associação 
# dos dados do livro com valores específicos.

# Usando um dicionário built-in para armazenar informações do livro

livros = {
'ISBN1': {'título': 'A Arte da Guerra', 'autor': 'Sun Tzu', 'ano': 500},
'ISBN2': {'título': '1984', 'autor': 'George Orwell', 'ano': 1949}
}

# Para gerenciar os empréstimos, você poderia definir uma classe personalizada, 
# pois os empréstimos podem envolver operações mais complexas que beneficiariam de 
# métodos específicos, como a atualização das datas de empréstimo e devolução ou o 
# cálculo de multas por atraso.

# Definindo uma classe personalizada para empréstimos

class Emprestimo:
    def __init__(self, livro, data_emprestimo, data_devolucao):
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

# Instanciando objetos da classe Emprestimo
emprestimo1 = Emprestimo(livros['ISBN1'], '2023-01-01', '2023-01-15') 
emprestimo2 = Emprestimo(livros['ISBN2'], '2023-02-01', '2023-02-15')

# A escolha entre estruturas de dados built-in e personalizadas depende das necessidades 
# específicas do sistema. No exemplo da biblioteca:

# Os dicionários built-in são adequados para armazenar informações dos livros, 
# pois oferecem uma maneira simples e eficiente de acessar e manipular dados associativos 
# sem a necessidade de funcionalidades adicionais.

# As estruturas de dados definidas pelo usuário, como a classe Emprestimo, 
# fornecem maior flexibilidade para incorporar lógicas de negócios complexas, 
# como métodos para manipular as datas dos empréstimos e calcular atrasos, 
# o que seria mais complicado de implementar com estruturas de dados built-in.

# Portanto, a decisão foi baseada na complexidade dos dados e operações 
# necessárias: o uso pragmático de dicionários built-in para informações 
# simples de livros e a criação de uma classe personalizada para gerenciar 
# a lógica específica de empréstimos.


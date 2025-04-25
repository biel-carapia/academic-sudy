import matplotlib.pyplot as plt
from collections import defaultdict
# Classe que cria um livro com os atributos titulo, genero e quantidade de livros disponíveis 
class Livro:
    def __init__(self, titulo, genero, qtd_disponivel):
        self.titulo = titulo
        self.genero = genero
        self.qtd_disponivel = qtd_disponivel

    def __str__(self):
        return f"Título do livro: {self.titulo}\nGenêro: {self.genero}\nQuantidade disponível: {self.qtd_disponivel}\n"


# Criar uma lista de livros
biblioteca = []

# Lista que armaezena a quantidade
qtd_livro_por_genero = []

# LIsta que armazena os generos
generos = []

# Função que recebe os dados do livro e cadastra eles
def cadastrar_livro(titulo, genero, qtd_disponivel):
    novo_livro = Livro(titulo, genero, qtd_disponivel)
    biblioteca.append(novo_livro)
    generos.append(genero)
    qtd_livro_por_genero.append(qtd_disponivel)
    print(f"O livro '{titulo}' foi adicionado à biblioteca.")

# Função para listar todos os livros na biblioteca
def listar_livros():
    print("\n======== Livros na Biblioteca ========\n")
    for livro in biblioteca:
        print(livro)
    print("======================================")

# Função que busca um livro pelo título
def buscar_livro(titulo):
    for livro in biblioteca:
        if(livro.titulo == titulo):
            print("Livro encontrado")
            print(livro)

# Adicionar alguns livros à biblioteca 
cadastrar_livro("Dom Quixote", "Romance", 2)
cadastrar_livro("A Ilíada de Homero", "Épica", 3)
cadastrar_livro("Romeu e Julieta de William Shakespeare", "Drama", 1)
cadastrar_livro("Os Sofrimentos do Jovem Werther de Johann Wolfgang von Goethe", "Romance", 5)
cadastrar_livro("Os Poemas de Fernando Pessoa", "Lírico ", 3)

# Listar todos os livros na biblioteca
listar_livros()

# Busca livro na biblioteca um livro com um título específico
buscar_livro("A Ilíada de Homero")


# Aqui criei uma variavel que soma a quantidade de livros por genêro
# Usei o defaultdict(int) para fornecer um valor padrão para uma chave inexistente no dicionário, 
# eliminando a necessidade de verificar se a chave existe antes de usá-la
soma_por_genero = defaultdict(int)
for genero, qtd in zip(generos, qtd_livro_por_genero):
    soma_por_genero[genero] += qtd

# Nessa parte começo a criar o gráfico da quantidade de livro disponível por genero separando os generos 
# e as quantidades somadas para plotar no gráfico
generos_unicos = list(soma_por_genero.keys())
quantidades_somadas = list(soma_por_genero.values())

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.bar(generos_unicos, quantidades_somadas, color='skyblue')
plt.title("Quantidade de Livros por Gênero")
plt.xlabel("Gênero")
plt.ylabel("Quantidade de Livros")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


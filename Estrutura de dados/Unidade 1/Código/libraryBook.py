class libraryVirtual:
    def __init__(self):
        # Dicionário para armazenar os livros. A chave é o título do livro.
        self.books = {}

    def add_books(self, title, author, year):
        if title in self.books:
            print("Livro já existe na biblioteca")
        else:
            self.books[title] = {'Autor' : author, 'Ano' : year}
            print("Livro adicionado.")
    
    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print("Livro removido.")
        else:
            print("Livro não encontrado.")

    def search_book(self, title):
        return self.books.get(title, "Livro não encontrado.")
    
    def list_book(self):
        for title, infos in self.books.items():
            print(f"{title}, de {infos['Autor']} {infos['Ano']}")



# Exemplo de uso
library = libraryVirtual()

library.add_books("Dom Casmurro", "Machado de Assis", 1899)
library.add_books("1984", "George Orwell", 1949)
print(library.search_book("Dom Casmurro"))
library.list_book()
library.remove_book("1984")
library.list_book
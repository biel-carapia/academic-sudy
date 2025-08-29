class ItemLista:
    # comumente referido como "dunder initdunderdouble underscoredata, 
    # que armazena o valor a ser incluído na lista, e nextItem, que guarda a referência ao próximo item na lista encadeada.
    def __init__(self, data=0, nextItem=None):
        self.data = data
        self.next = nextItem
    # fornece uma representação em string do objeto, exibindo o item adicionado e o próximo item na sequência.
    def __repr__(self):
        return '%s => %s' % (self.data, self.next)
    

# Quando essa classe é instanciada, um único objeto, chamado de ‘head’, é inicializado. 
# Esse objeto 'head' serve como indicador do primeiro item na lista encadeada. 
# Ademais, na classe 'ListaEncadeada', implementaremos métodos adicionais que facilitarão a inserção, remoção e localização de elementos na lista.
class ListaEncadeada:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "%s" % (self.head)
    
    def insere(lista, data):
        # cria um objeto para armazenar um novo item da lista
        item = ItemLista(data)
        # o head é apontado como próximo item
        item.next = lista.head
        # o item atual se torna o head
        lista.head = item


    def remove(lista, valor):
        # verifica se o item a ser removido é o head
        if lista.head and lista.head.data == valor:
            lista.head = lista.head.next
        else:
            # Detecta a posição do elemento
            before = None
            navegar = lista.head
            # Navega pela lista para encontrar o elemento
            
            while navegar and navegar.data != valor:
                before = navegar
                navegar = navegar.next

            #print(navegar.data)
            # Remove o item se ele for encontrado
            if navegar:
                before.next = navegar.next

    def buscar(lista, valor):
        navegar = lista.head
        while navegar and navegar.data != valor:
            navegar = navegar.next
        return navegar



'''
    AGORA VAMOS VER COMO UTILIZAR ESTE CÓDIGO:
''' 

lista = ListaEncadeada()
lista.insere(1)
lista.insere(2)
lista.insere(3)

print("Lista apos a insercao: ", lista)

lista.remove(2)
print("Lista apos remocer o valor 2: ", lista)

item_encontrado = lista.buscar(3)
if item_encontrado:
    print("Item encontrado:", item_encontrado)
else: 
    print("Item não encontrado.")

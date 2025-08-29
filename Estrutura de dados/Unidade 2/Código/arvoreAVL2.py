class VerticeAVL: 
  # Construtor: inicializa um vértice com uma chave, pai e subárvores esquerda e direita vazias. 
  def __init__(self, chave, pai=None): 
    self.chave = chave # Valor do nó 
    self.pai = pai # Referência ao pai 
    self.esquerdo = None # Subárvore esquerda 
    self.direito = None # Subárvore direita 
    self._altura = 0 # Altura do nó, inicialmente 0 

  # Métodos __str__ e __repr__ para representar o vértice com sua chave. 
  def __str__(self): 
    return str(self.chave) 

  def __repr__(self): 
    return str(self.chave) 

  # Método para imprimir a subárvore a partir deste vértice, com recuo visual para indicar a hierarquia. 
  def imprimir_subarvore(self, recuo=0, sentido=0): 
    if self.direito: 
      self.direito.imprimir_subarvore(recuo+10, sentido)   
    print( 
      "{}{}----> [{}] (h={},fb={})".format( 
        * recuo, 
        sentido, 
        self.chave, 
        self.altura, 
        self.fator_de_balanceamento, 
      )
    ) 
    if self.esquerdo: 
        self.esquerdo.imprimir_subarvore(recuo+10, sentido="\\") 

  # Método para inserir uma nova chave na árvore, respeitando as propriedades de árvore AVL. 
  def inserir(self, chave_nova): 
    print("{} (atual={})".format(chave_nova, self.chave)) 
    if chave_nova == self.chave: 
      return self # Se a chave já existe, não faz nada.

    raiz_da_subarvore = self 
    # Insere na subárvore esquerda ou direita, conforme a comparação das chaves. 
    if chave_nova < self.chave: 
      if self.esquerdo: 
        raiz_da_subarvore = self.esquerdo.inserir(chave_nova) 
      else: 
        self.esquerdo = VerticeAVL(chave_nova, self) 
    elif chave_nova > self.chave: 
      if self.direito: 
        raiz_da_subarvore = self.direito.inserir(chave_nova) 
      else: 
        self.direito = VerticeAVL(chave_nova, self) 

    # Atualiza a altura e balanceia a árvore após a inserção. 
    raiz_da_subarvore.atualizar_altura() 
    raiz_da_subarvore = raiz_da_subarvore.balancear() 
    return raiz_da_subarvore.pai or raiz_da_subarvore # Retorna a nova raiz da subárvore. 
  
    def _remover_folha(self): 
        """
        Remove o vértice folha 
        :return: nova raiz 
        """ 
        print("{}, vértice folha, filho de {}".format( 
        self.chave, self.pai.chave)) 
        pai = self.pai 
        if self.pai: 
            # tem pai, então não sou a raiz 
            if self.pai.esquerdo is self: 
                # sou filho da esquerda, me desvincula da esquerda  
                self.pai.esquerdo = None 
        else: 
            # sou filho da direita, me desvincula da direita 
            self.pai.direito = None 
            # me desvinculo do meu pai 
            self.pai = None 
        return pai 

    def _remover_pai_de_um_filho(self): 
        """
        Remove o vértice que tem um filho direito ou esquerdo 
        :return: nova raiz 
        """ 
        print("{}, pai de {}".format( 
        self.chave, (self.esquerdo or self.direito).chave)) 
        # identifico meu pai 
        meu_pai = self.pai 
        # tenho só 1 filho, identifico meu filho (esquerdo ou direito) 
        meu_filho = self.esquerdo or self.direito 

        if meu_pai is None: 
            # sou raiz, a árvore está apontando para mim, 
            # não posso ser removido 
            # então, vou trocar de lugar com meu filho 
            meu_filho.chave, self.chave = self.chave, meu_filho.chave 
            # agora estou no lugar do meu filho e posso ser removido 
            # a recursividade tratará a forma como serei removido 
            return meu_filho.remover(meu_filho.chave) 
        # meu pai, é pai do meu filho 
        meu_filho.pai = meu_pai 
        # meu filho, passa a ser filho do meu pai 
        if meu_pai.esquerdo is self: 
            # sou filho da direita, 
            # meu filho passa a ser seu filho da direita 
            meu_pai.esquerdo = meu_filho 
        else: 
            # sou filho da esquerda, 
            # meu filho passa a ser seu filho da esquerda 
            meu_pai.direito = meu_filho 

        # me desvinculo do meu pai e do meu filhho 
        self.pai = None 
        self.esquerdo = None 
        self.direito = None 
        return meu_pai 

    def _remover_pai_de_dois_filhos(self): 
        """
        Remove o vértice que tem 2 filhos 
        :return: nova raiz 
        """ 

        print("{}, pai de {} e {}".format( 
        self.chave, self.esquerdo.chave, self.direito.chave)) 
        # obter o vértice que tem a chave com menor valor (mais à esquerda) 
        # na subárvore do subarvore direita 
        esq = self.direito.buscar_vertice_menor_chave_na_subarvore() 
        print("{}".format(str(esq)))

        # troca valor da chave entre o nó atual e o esq 
        print("{} e {} trocam de vértice".format(self.chave, esq.chave)) 
        self.chave, esq.chave = esq.chave, self.chave 

        # remover o esquerdo / recursividade 
        return esq.remover(esq.chave) 

    def remover(self, chave): 
        print("{} (chave atual: {})".format(chave, self.chave)) 
        if self.chave == chave: 
            print("{} para remover".format(chave)) 
            # encontrou a chave a ser removida 

        if self.esquerdo and self.direito: 
            # tem ambos filhos 
            raiz_da_subarvore = self._remover_pai_de_dois_filhos() 
        elif self.esquerdo or self.direito: 
            # tem ou filho esquerdo ou filho direito 
            raiz_da_subarvore = self._remover_pai_de_um_filho() 
        else: 
            # nao tem filhos 
            raiz_da_subarvore = self._remover_folha() 
        # retorna o pai 
        return raiz_da_subarvore 

        raiz_da_subarvore = self 
        if chave < self.chave: 
            # se esquerdo existe, continua a busca pelo esquerdo 
            # senão a busca encerra e None é retornado 
            raiz_da_subarvore = self.esquerdo and self.esquerdo.remover(chave) 
        elif chave > self.chave: 
            # se direito existe, continua a busca pelo direito 
            # senão a busca encerra e None é retornado 
            raiz_da_subarvore = self.direito and self.direito.remover(chave) 
            
        if raiz_da_subarvore: 
            raiz_da_subarvore.atualizar_altura() 
            raiz_da_subarvore = raiz_da_subarvore.balancear() 
            # retorna o pai do raiz_da_subarvore se existir, senão retorna raiz_da_subarvore 

        return raiz_da_subarvore.pai or raiz_da_subarvore 

    

    def buscar_vertice_menor_chave_na_subarvore(self): 
        """
        Procura o vértice que tem a menor chave na subárvore, 
        ou seja, o vértice que esteja à extrema esquerda na subárvore 
        """ 
        print("{}".format(str(self))) 
        if self.esquerdo: 
            # recursividade 
            return self.esquerdo.buscar_vertice_menor_chave_na_subarvore() 
        return self
    
    @property 
    def altura(self): 
        return self._altura 

    def atualizar_altura(self): 
        # pega a maior altura entre as duas subárvores e soma 1 
        self._altura = 1 + max([self.altura_esquerda, self.altura_direita]) 

    @property 
    def altura_esquerda(self): 
        if self.esquerdo: 
            return self.esquerdo.altura 
        return -1 

    @property 
    def altura_direita(self): 
        if self.direito: 
            return self.direito.altura 
        return -1 

    @property 
    def fator_de_balanceamento(self): 
        return self.altura_direita - self.altura_esquerda 

    def balancear(self): 
        fb = self.fator_de_balanceamento 
        print("{})={}".format(self.chave, fb)) 
        if fb == 2: 
            return self._balancear_subarvore_direita() 
        if fb == -2: 
            return self._balancear_subarvore_esquerda() 
        return self 

    def _balancear_subarvore_direita(self): 
        print({}.format(self.chave)) 
        if self.direito.fator_de_balanceamento == -1: 
            # Caso RL: aplicar rotacao do filho direito para a direita 
            # para ficar com a configuração do Caso RR 
            print("{} à direita + Rotação de {} à esqueda".format( 
            str(self.direito), self.chave) 
            ) 
        self.direito._rotacao_para_direita() 
        # Caso RR: aplicar rotacao a esquerda 
        nova_raiz = self._rotacao_para_esquerda() 
        return nova_raiz 

    def _balancear_subarvore_esquerda(self): 
        print({}.format(self.chave)) 
        if self.esquerdo.fator_de_balanceamento == 1: 
            # Caso LR: aplicar rotacao do filho esquerdo para a esquerda 
            # para ficar com a configuração do Caso LL 
            print("{} à esquerda + Rotação de {} à direita".format( 
                str(self.esquerdo), self.chave) 
            ) 
        self.esquerdo._rotacao_para_esquerda() 
        # Caso LL: aplicar rotacao direita 
        nova_raiz = self._rotacao_para_direita() 
        return nova_raiz 

    def _rotacao_para_esquerda(self): 
        """
        Caso RR (Right Right Case) - rotação única 

        Caso LR (Left Right Case) - primeira rotação     

         v1               v2 

        / \\            /   \\ 

         s1  v2           v1     v3 

        / \\    ->    / \\   / \\ 

        s2  v3         s1  s2   s3  s4 

            / \\ 

        s3   s4 

        """ 
        self._rotacao_info() 
        # identifica os vértices envolvidos: 
        # pai da subarvore, v1 (raiz da subarvore), v2 (nova raiz da subarvore) e s2  
        raiz_da_subarvore = self 
        pai_da_subarvore = raiz_da_subarvore.pai 
        v1 = raiz_da_subarvore 
        v2 = v1.direito 
        s2 = v2.esquerdo 

        # executa a rotação / atualiza os relacionamentos entre os vértices 
        if pai_da_subarvore: 
            if raiz_da_subarvore is pai_da_subarvore.direito: 

                # raiz da subarvore é filho direito  

                pai_da_subarvore.direito = v2 
            else: 
                pai_da_subarvore.esquerdo = v2 
        v1.pai = v2 
        v1.direito = s2 
        v2.pai = pai_da_subarvore 
        v2.esquerdo = v1 
        if s2: 
            s2.pai = v1 

        # atualizar alturas 
        v1.atualizar_altura() 
        v2.atualizar_altura() 

        self._rotacao_info(v2) 

        # retorna a nova raiz 

        return v2 

    

    def _rotacao_para_direita(self): 
        """
        Caso LL (Left Left Case) - rotação única 

        Caso RL (RightLeft Case) - primeira rotação 

            |              | 

            v3 (self)          v2 

            / \\           /  \\ 

         v2  s4     ->    v1    v3 

        / \\          / \\   / \\ 

        v1  s3          s1  s2   s3  s4 

        / \\ 

        s1  s2 

        """ 

        self._rotacao_info(sentido=0)     
        # identfica os vértices envolvidos 
        raiz_da_subarvore = self 
        v3 = raiz_da_subarvore 
        pai_da_subarvore = raiz_da_subarvore.pai 
        v2 = v3.esquerdo 
        s3 = v2.direito

        # Faz a rotação / atualiza os relacionamentos entre os vértices 
        if pai_da_subarvore: 
            if raiz_da_subarvore is pai_da_subarvore.direito: 

                pai_da_subarvore.direito = v2 
        else: 
            pai_da_subarvore.esquerdo = v2 

        v2.pai = pai_da_subarvore 
        v2.direito = v3 
        v3.pai = v2 
        v3.esquerdo = s3 

        if s3: 
            s3.pai = v3 

        # atualizar alturas 
        v3.atualizar_altura() 
        v2.atualizar_altura()

        self._rotacao_info(v2) 

        # retorna a nova raiz 
        return v2 

    

    def _rotacao_info(self, sentido, nova_raiz_da_subarv=None): 
        print() 
        if nova_raiz_da_subarv is None: 
            caso = if sentido == else  
            print("{}: Rotação de {} à {}".format(caso, sentido, self.chave)) 
            print() 
        else: 
            print() 

        atual = nova_raiz_da_subarv or self 
        (atual.pai or atual).imprimir_subarvore() 
        print() 

        if nova_raiz_da_subarv: 
            print("{} à {}: nova_raiz={} (pai={})".format(  
            self.chave, 
            sentido, 
            str(nova_raiz_da_subarv), 
            str(nova_raiz_da_subarv.pai)))
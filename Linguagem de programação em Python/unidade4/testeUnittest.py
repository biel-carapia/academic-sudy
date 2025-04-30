import unittest

def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2,3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

if __name__ == '__mian__':
    import unittest
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    print("Os testes foram executados com sucesso")


# A função add simplesmente soma dois números, cria uma classe que herda de unittest.TestCase.
# Isso indica que essa classe contém testes unitários.
# Dentro da classe de testes, você define métodos de teste.
# Cada método de teste deve começar com a palavra-chave test.
# Dentro desses métodos, você usa assertivas (como self.assertEqual) para verificar se o comportamento esperado do código é atendido.
# A condição if __name__ == '__mian__': garante que o suíte de testes seja executada somente se o script for executado diretamente
# não se for importado como um módulo em outro script). unittest.main() executa todos os testes definidos na classe TestAddition. 
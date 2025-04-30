import doctest


def square(x):
    """
    Retorna o quadrado de um número.

    Exemplo:
    >>> square(3)
    9
    >>> square(-2)
    4
    >>> square(0)
    0
    """
    return x * x

doctest.testmod()


#A função square é acompanhada por uma string de documentação que inclui exemplos de uso.
#Esses exemplos estão formatados de maneira especial, usando o prompt >>>, que indica um bloco de código Python.

#No caso do exemplo, doctest.testmod() executará a função square(3),
#verificará se o resultado é igual a 9, executará square(-2) e verificará se o resultado é 4, e assim por diante

#Se todos os testes passarem, doctest não produzirá nenhuma saída.
#Se houver uma discrepância entre a saída real e a esperada, doctest imprimirá uma mensagem indicando onde ocorreu o problema.

#A principal vantagem do doctest é que ele permite que você mantenha exemplos na documentação e, ao mesmo tempo, use esses exemplos como testes automáticos.
#Isso ajuda a garantir que a documentação esteja sempre na sincronia com o código real
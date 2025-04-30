#doctest
def sum_numbers(numbers):
    """
    Soma os números em uma lista.

    Exemplos:
    >>> sum_numbers([1, 2, 3, 4])
    10
    >>> sum_numbers([-1, 0, 1])
    0
    >>> sum_numbers([])
    0    
    """
    return sum(numbers)

if __name__ == '__main__':
    import doctest
    doctest.testmod()



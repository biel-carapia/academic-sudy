#assert
def sum_numbers(numbers):
    assert sum([1, 2, 3, 4]) == 10
    assert sum([-1, 0, 1]) == 0
    assert sum([]) == 0
    return sum(numbers)
teste = sum_numbers([1, 2, 3, 4, 5])
print(teste)

try:
    print(1 + 'a')
except:
    print('Um erro foi encontrado')



try:
    print(1 + 'a')
except TypeError:
    print('Um erro de tipo foi encontrado')



try:
    int('a')
except TypeError:
    print('Um erro de tipo foi encontrado')
except ValueError:
    print('Um erro de valor foi encontrado') 
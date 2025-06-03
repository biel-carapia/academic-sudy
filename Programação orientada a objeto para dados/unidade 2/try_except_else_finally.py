try:
    int('1')
except TypeError:
    print('Um erro de tipo foi encontrado')
except ValueError:
    print('Um erro de valor foi encontrado')
else:
    print('Nenhum erro foi encontrado')


try:
    arquivo = open('arquivo.txt', 'r')
    # Realiza alguma operação no arquivo
    print(arquivo.read())
except FileNotFoundError:
    print('O arquivo não foi encontrado.')
finally:
    # Garante que o arquivo seja sempre fechado, mesmo se ocorrer uma exceção
    arquivo.close()



with open('workfile', encoding="utf-8") as f:
    read_data = f.read()
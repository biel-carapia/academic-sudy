# Bem vindo à Máquina de venda Automática de Ingressos de Cinema!

# Solicita a idade do cliente
idade = int(input("Por favor, digite sua idade: "))

# Verifica a idade para sugestão de filmes
if idade < 12:
    print("Recomendamos o filme infatil FILME 1.")
elif 12 <= idade < 18:
    print("Recomendamos o filme infatil FILME 2.")
else:
    print("Recomendamos o emocionante FILME 3.")

# Verifica a disponibilidade do ingesso
quantidade_ingressos = 10 # Suponha que haja 10 ingressos disponíveis
if quantidade_ingressos > 0:
    print("Ingressos estão disponíveis. Divirta-se no cinema!")
else:
    print("Desculpe, todos os ingressos estão esgotados para hoje.")





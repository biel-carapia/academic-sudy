import matplotlib.pyplot as plt

# Dados de exemplo
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']
vendas = [120, 90, 150, 80, 200]

# Criar um gráfico de barras
plt.bar(meses, vendas, coldr='royalblue')

# Adicionar um título ao gráfico
plt.title('Vendas Mensais')

#Mostrar o gráfico
plt.show

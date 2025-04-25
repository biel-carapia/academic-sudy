import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

df = sns.load_dataset('tips')

plt.figure(figsize=(8, 5)) #Fazendo um gráfico
sns.barplot(x='time', y='total_bill', data=df, estimator=sum, ci=None, palette="Set2") #Total de gastos por periodo
plt.xlabel('Período (Time)')
plt.ylabel('Total de Gastos')
plt.title('Total de Gastos por Período (Almoço ou Jantar)')
plt.show()


plt.figure(figsize=(8, 5))
sns.barplot(x='time', y='total_bill', data=df) #Quando quremos mostrar a média, não precisa colocar o estimator
plt.xlabel('Período (Time)')
plt.ylabel('Média de Gastos')
plt.title('Média de Gastos por Período (Almoço ou Jantar)')
plt.show()


# Crie um gráfico de barras com Seaborn para mostrar a média da gorjeta por período
plt.figure(figsize=(8, 5))
sns.barplot(x='time', y='total_bill', data=df, palette="Set2")
plt.xlabel('Período (Time)')
plt.ylabel('Média de Gorjeta')
plt.title('Média de Gorjeta por Período (Almoço ou Jantar)')
plt.show()
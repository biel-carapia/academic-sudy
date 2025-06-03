# Por exemplo, podemos criar uma classe Plotter que recebe os dados e parâmetros 
# necessários para plotar um determinado tipo de gráfico. Essa classe pode ter 
# métodos para configurar o estilo, adicionar títulos e rótulos, e plotar o gráfico em si.


import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, data, title=None, xlabel=None, ylabel=None):
        self.data = data
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
 

    def plot_histogram(self, bins=10, color='blue'):
        plt.hist(self.data, bins=bins, color=color)
        self._set_labels()
        plt.show()
 

    def plot_bar(self, xticks_rotation=0, color='green'):
        plt.bar(self.data.index, self.data.values, color=color)
        plt.xticks(rotation=xticks_rotation)
        self._set_labels()
        plt.show()

 
    def _set_labels(self):
        if self.title:
            plt.title(self.title)
        if self.xlabel:
            plt.xlabel(self.xlabel)
        if self.ylabel:
            plt.ylabel(self.ylabel)


# Exemplo de uso
data = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8, 9, 10]
plotter = Plotter(data, title='Exemplo de Histograma', xlabel='Valores', ylabel='Frequência')
plotter.plot_histogram(bins=5, color='red')
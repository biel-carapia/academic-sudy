class Cartao():

    def __init__(self):
        self._limite = 100

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        if limite < 0:
            raise ValueError('O limite não pode ser negativo')
        else:
            self._limite = limite


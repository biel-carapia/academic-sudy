from abc import ABC, abstractmethod

class ExtratorBase(ABC):
    def carregar_documento(self):
        "Esta função irá carregar o pdf ou imagem para o sistema."
        pass

    @abstractmethod
    def extrair_texto(self):
        raise NotImplementedError


class ExtratorPDF(ExtratorBase):
    def extrair_texto(self):
        "Implementação do algoritmo para extração de texto de um pdf."
        pass

class ExtratorImagem(ExtratorBase):
    def extrair_texto(self):
        "implementação do algoritmo para extração de texto de uma imagem."
        pass



#resolucao situacao problema

class Prontuario:
    def __init__(self, paciente, diagnostico, tratamento, proximo=None):
        self.paciente = paciente
        self.diagnostico = diagnostico
        self.tratamento = tratamento
        self.proximo = proximo


class ListaEncadeadaProntuarios:
    def __init__(self):
        self.cabeca = None

 

def adicionar_prontuario(self, paciente, diagnostico, tratamento):
    novo_prontuario = Prontuario(paciente, diagnostico, tratamento, self.cabeca)
    self.cabeca = novo_prontuario

 

def buscar_prontuario(self, nome_paciente):
    atual = self.cabeca
    while atual:
        if atual.paciente == nome_paciente:
            return atual
        atual = atual.proximo

    return None


# Uso da lista encadeada para gerenciar prontuários
sistema_prontuarios = ListaEncadeadaProntuarios()
sistema_prontuarios.adicionar_prontuario("Alice Santos", "Diabetes Tipo 2", "Metformina")
sistema_prontuarios.adicionar_prontuario("João Silva", "Hipertensão", "Losartana")

# Adicionar mais prontuários conforme necessário

# Buscando um prontuário
prontuario_alice = sistema_prontuarios.buscar_prontuario("Alice Santos")
class Arquivo:
    def __init__(self, dados_arquivo):
        self.nome = dados_arquivo[0]
        self.inicio = int(dados_arquivo[1])
        self.tamanho = int(dados_arquivo[2])


class OperacaoArquivo:
    def __init__(self, dados_operacao):
        self.PID = int(dados_operacao[0])
        self.cod_operacao = int(dados_operacao[1])
        self.nome = dados_operacao[2].rstrip()
        if(len(dados_operacao) == 4):
            self.tamanho = int(dados_operacao[3])
        else:
            self.tamanho = 0

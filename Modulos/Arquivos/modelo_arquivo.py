class Arquivo:
    def __init__(self, dados_arquivo):
        self.nome = dados_arquivo[0]
        self.inicio = dados_arquivo[1]
        self.tamanho = dados_arquivo[2]

class OperacaoArquivo:
    def __init__(self, dados_operacao):
        self.id_processo = dados_operacao[0]
        self.cod_operacao = dados_operacao[1]
        self.nome_arquivo = dados_operacao[2]
        if(len(dados_operacao)==4):
          self.num_blocos = dados_operacao[3]
        else:
          self.num_blocos = 0
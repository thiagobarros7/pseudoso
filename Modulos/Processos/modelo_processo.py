class Processo:
    def __init__(self, dados_processo):
        self.tempo_de_inicializacao = dados_processo[0]
        self.prioridade = dados_processo[1]
        self.tempo_de_processador = dados_processo[2]
        self.blocos_em_memoria = dados_processo[3]
        self.cod_impressora = dados_processo[4]
        self.scanner = dados_processo[5]
        self.modem = dados_processo[6]
        self.cod_disco = dados_processo[7]

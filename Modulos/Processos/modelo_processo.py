class Processo:
    def __init__(self, dados_processo):
        self.tempo_de_inicializacao = int(dados_processo[0])
        self.prioridade = int(dados_processo[1])
        self.tempo_de_processador = int(dados_processo[2])
        self.blocos_em_memoria = int(dados_processo[3])
        self.cod_impressora = int(dados_processo[4])
        self.scanner = int(dados_processo[5])
        self.modem = int(dados_processo[6])
        self.cod_disco = int(dados_processo[7])
        self.PID = 0
        self.offset = 0
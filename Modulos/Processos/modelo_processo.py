class Processo:
    def __init__(self, tempo_de_inicializacao, prioridade, tempo_de_processador,
                 blocos_em_memoria, cod_impressora, scanner, modem, cod_disco):
        self.tempo_de_inicializacao = tempo_de_inicializacao
        self.prioridade = prioridade
        self.tempo_de_processador = tempo_de_processador
        self.blocos_em_memoria = blocos_em_memoria
        self.cod_impressora = cod_impressora
        self.scanner = scanner
        self.modem = modem
        self.cod_disco = cod_disco

class Processo:
    def __init__(self, dados_processo):
        self.tempo_de_inicializacao = int(dados_processo[0])
        self.prioridade = int(dados_processo[1])
        self.tempo_de_processador = int(dados_processo[2])
        self.blocos_em_memoria = int(dados_processo[3])
        self.recursos = {}
        self.recursos['cod_impressora'] = int(dados_processo[4])
        self.recursos['scanner'] = int(dados_processo[5])
        self.recursos['modem'] = int(dados_processo[6])
        self.recursos['cod_disco'] = int(dados_processo[7])
        self.PID = -1
        self.offset = 0
        self.numero_instrucao = 1
        self.execucao = 0

    def executa_processo(recursos):
        print("P"+str(processo.PID)+" STARTED")
        recursos.requisita_recurso(processo.recursos)
        print("P"+str(processo.PID)+" instruction "+str(i))
        time.sleep(1)
        if self.numero_instrucao == self.tempo_de_processador:
            recursos.desaloca_recurso(processo.recursos)
            print("P"+str(processo.PID)+" return SIGINT")

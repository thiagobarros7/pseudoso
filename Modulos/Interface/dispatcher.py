class Despachante:
    def __init__(self):
        self.tempos_de_processador = []
        self.flag_usuario = []
        self.proximo_PID = 0
    
    def despacha_processo(self, processo):
        if processo.PID == -1:
            processo.PID = self.proximo_PID
            self.proximo_PID += 1
            print('dispatcher =>')
            print('PID: ' + str(processo.PID))
            print('offset: ' + str(processo.offset))
            print('blocos: ' + str(processo.blocos_em_memoria))
            print('prioridade: ' + str(processo.prioridade))
            print('tempo: ' + str(processo.tempo_de_processador))
            print('impressoras: ' + str(processo.recursos['cod_impressora']))
            print('scanners: ' + str(processo.recursos['scanner']))
            print('modems: ' + str(processo.recursos['modem']))
            print('satas: ' + str(processo.recursos['cod_disco']))
            if processo.prioridade:
                self.flag_usuario.append(1)
            else:
                self.flag_usuario.append(0)
            self.tempos_de_processador.append(processo.tempo_de_processador)
            return(1)
        return(0)

    def executa_sistema_de_arquivos(self, disco):
        print('Sistema de arquivos =>')
        resultados = disco.executa_operacoes(self.tempos_de_processador, self.flag_usuario)
        for index, resultado in enumerate(resultados):
            print('Operação ' + str(index) + ' => ' + resultado['status'])
            print(resultado['texto'])
        print('Mapa de ocupação do disco:')
        print(disco.blocos)

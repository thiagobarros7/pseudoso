class Disco:
    def __insere_arquivos_iniciais(self):
        for arquivo in self.arquivos:
            for i in range(arquivo.inicio, arquivo.inicio+arquivo.tamanho):
                self.blocos[i] = arquivo.nome
        return 1

    def __init__(self, arquivos_lidos):
        self.blocos = [0]*arquivos_lidos['blocos_disco']
        self.arquivos = arquivos_lidos['arquivos']
        self.operacoes = arquivos_lidos['operacoes']
        self.tempos_de_processador = {}
        self.flag_usuario = {}
        self.dono_arquivo = {}
        self.__insere_arquivos_iniciais()

    def __busca_espaco_vazio(self, tamanho_arquivo):
        espaco_contiguo_vazio = 0
        espacos_vazios = 0
        for i in range(len(self.blocos)):
            if self.blocos[i]:
                espacos_vazios = 0
            else:
                espacos_vazios += 1
                if espacos_vazios > espaco_contiguo_vazio:
                    espaco_contiguo_vazio = espacos_vazios
                    if espaco_contiguo_vazio == tamanho_arquivo:
                        return i+1-tamanho_arquivo
        return (-1)

    def __busca_arquivo(self, nome):
        tamanho_arquivo = 0
        primeira_ocorrencia = 0
        inicio_arquivo = 0
        for i in range(len(self.blocos)):
            if(self.blocos[i] == nome):
                if not primeira_ocorrencia:
                    inicio_arquivo = i
                    primeira_ocorrencia = 1
                tamanho_arquivo += 1
        return(primeira_ocorrencia, inicio_arquivo, tamanho_arquivo)

    def __operacao_inserir(self, operacao):
        offset = self.__busca_espaco_vazio(operacao.tamanho)
        if offset != -1:
            for i in range(offset, offset+operacao.tamanho):
                self.blocos[i] = operacao.nome
            return (offset)
        else:
            return (-1)

    def __operacao_deletar(self, operacao):
        arquivo_achado, inicio_arquivo, tamanho_arquivo = self.__busca_arquivo(
            operacao.nome)
        if not arquivo_achado:
            ("Arquivo inexistente!")
            return(0)
        for i in range(inicio_arquivo, tamanho_arquivo):
            self.blocos[i] = 0
        return(1)

    def __verifica_processo_usuario(self, PID):
        if self.flag_usuario[str(PID)]:
            return(1)
        return(0)

    def __verifica_dono_arquivo(self, PID, nome_arquivo):
        if nome_arquivo in self.dono_arquivo:
            if self.dono_arquivo[nome_arquivo] == str(PID):
                return(1)
        return(0)

    def __cadastra_dono_arquivo(self, PID, nome_arquivo):
        if nome_arquivo in self.dono_arquivo:
            return(0)
        else:
            self.dono_arquivo[nome_arquivo] = PID
            return(1)

    def __verifica_tempo_de_processador(self, PID):
        if self.tempos_de_processador[str(PID)] > 0:
            return(1)
        return(0)

    def __verifica_processo(self, PID):
        if str(PID) in self.tempos_de_processador:
            return (1)
        return(0)

    def __executa_operacao(self, operacao):
        if self.__verifica_processo(operacao.PID):
            if self.__verifica_tempo_de_processador(operacao.PID):
                self.tempos_de_processador[str(operacao.PID)] -= 1
                if (not operacao.cod_operacao and operacao.tamanho):
                    offset = self.__operacao_inserir(operacao)
                    if not self.__cadastra_dono_arquivo(operacao.PID, operacao.nome):
                        return({'status': 'Falha', 'texto': 'Já existe um arquivo com o mesmo nome, operação de inserção cancelada'})
                    if offset != -1:
                        for bloco_ocupado in range(offset, offset+operacao.tamanho):
                            if bloco_ocupado == offset:
                                texto_blocos = 'blocos ' + str(bloco_ocupado)
                            else:
                                texto_blocos += ', ' + str(bloco_ocupado)
                        return({'status': 'Sucesso', 'texto': 'O processo ' + str(operacao.PID) + ' criou o arquivo ' + operacao.nome + ' (' + texto_blocos + ').'})
                    else:
                        return({'status': 'Falha', 'texto': 'O processo ' + str(operacao.PID) + ' não pode criar o arquivo ' + operacao.nome + ' (falta de espaço).'})
                else:
                    if self.__verifica_processo_usuario(operacao.PID):
                        if not self.__verifica_dono_arquivo(operacao.PID, operacao.nome):
                            return({'status': 'Falha', 'texto': 'Processo de usuáio não é dono do arquivo, operação cancelada.'})
                    if self.__operacao_deletar(operacao):
                        return({'status': 'Sucesso', 'texto': 'O processo ' + str(operacao.PID) + ' deletou o arquivo ' + operacao.nome + '.'})
                    else:
                        return({'status': 'Falha', 'texto': 'Arquivo inexistente!'})
            else:
                return({'status': 'Falha', 'texto': 'Operação não realizada por falta de tempo de processador'})
        else:
            return({'status': 'Falha', 'texto': 'Não existe o processo.'})

    def executa_operacoes(self, tempos_de_processador, flag_usuario):
        self.tempos_de_processador = tempos_de_processador
        self.flag_usuario = flag_usuario
        status_operacoes = []
        for operacao in self.operacoes:
            status_operacoes.append(self.__executa_operacao(operacao))
        return status_operacoes

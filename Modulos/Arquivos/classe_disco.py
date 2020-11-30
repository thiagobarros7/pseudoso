class Disco:
    def __init__(self, arquivos_lidos):
        self.blocos = [0]*arquivos_lidos['blocos_disco']
        self.arquivos = arquivos_lidos['arquivos']
        self.operacoes = arquivos_lidos['operacoes']

    def insere_arquivos_iniciais(self):
        for arquivo in self.arquivos:
            for i in range(arquivo.inicio, arquivo.inicio+arquivo.tamanho):
                self.blocos[i] = arquivo.nome
        return 1

    def __busca_espaco_vazio(self, tamanho_arquivo):
        espaco_contiguo_vazio = 0
        espacos_vazios = 0
        for i in range(len(self.blocos)):
            if not self.blocos[i]:
                espacos_vazios += 1
                if espacos_vazios > espaco_contiguo_vazio:
                    espaco_contiguo_vazio = espacos_vazios
                    if espaco_contiguo_vazio == tamanho_arquivo:
                        return i+1-tamanho_arquivo
            else:
                espacos_vazios = 0
        return -1


    def __busca_arquivo(self, nome):
        tamanho_arquivo = 0
        primeira_ocorrencia = 0
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
            for i in range(operacao.tamanho):
                self.blocos[i] = operacao.nome
            return (1)
        else:
            return (0)

    def __operacao_deletar(self, operacao):
        arquivo_achado, inicio_arquivo, tamanho_arquivo = self.__busca_arquivo(operacao.nome)
        if not arquivo_achado:
            ("Arquivo inexistente!")
            return(0)
        for i in range(inicio_arquivo, tamanho_arquivo):
            self.blocos[i] = 0
        return(1)

    def __executa_operacao(self, operacao):
        if (not operacao.cod_operacao and not operacao.tamanho):
            if self.__operacao_deletar(operacao):
                return({'status': 1, 'texto': 'O processo ' + operacao.id_processo + ' \
                    deletou o arquivo ' + operacao_nome + '.'})
            else:
                return({'status': 0, 'texto': 'Arquivo inexistente!'})
        else:
            offset = self.__operacao_inserir(operacao)
            if offset:
                texto_blocos = 'blocos'
                for bloco_ocupado in range(offset, operacao.tamanho):
                    texto_blocos += ', ' + str(bloco_ocupado)
                return({'status': 1, 'texto': 'O processo ' + operacao.id_processo + ' \
                    criou o arquivo ' + operacao.nome + ' (' + texto_blocos + ').'})
            else:
                return({'status': 0, 'texto': 'O processo ' + operacao.id_processo + ' \
                    não pode criar o arquivo ' + operacao.nome + ' (falta de espaço).'})

    def executa_operacoes(self):
        status_operacoes = []
        for operacao in self.operacoes:
            status_operacoes.append(self.__executa_operacao(operacao))
        return status_operacoes

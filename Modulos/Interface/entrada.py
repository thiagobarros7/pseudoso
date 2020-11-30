from pathlib import Path


def le_processos():
    from Modulos.Processos.modelo_processo import Processo

    processos_objeto = []

    path = Path(__file__).parent / "../../Arquivos/processes.txt"
    with path.open() as arquivo:
        for processo in arquivo:
            processos_objeto.append(Processo(processo.split(', ')))
    return(processos_objeto)


def le_arquivos():
    from Modulos.Arquivos.modelo_arquivo import Arquivo, OperacaoArquivo

    i = 0
    arquivos = []
    operacoes = []
    path = Path(__file__).parent / "../../Arquivos/files.txt"
    with path.open() as arquivo:
        for linha in arquivo:
            if(i < 2):
                if(i == 0):
                    blocos_disco = int(linha)
                else:
                    numero_arquivos = int(linha)
            elif(i < numero_arquivos + 2):
                arquivos.append(Arquivo(linha.split(',')))
            else:
                operacoes.append(OperacaoArquivo(linha.split(',')))
            i = i+1
    arquivos = {'blocos_disco': blocos_disco, 'numero_arquivos': numero_arquivos,
                'arquivos': arquivos, 'operacoes': operacoes}
    return(arquivos)

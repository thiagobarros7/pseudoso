import threading
import time
import operator
from Modulos.Processos.thread_processo import executa_processo
from Modulos.Interface.dispatcher import Despachante

def inicia_processos(processos, fila):
    processos = sorted(processos, key=operator.attrgetter('tempo_de_inicializacao'))
    tempo_de_inicializacao_anterior = 1
    for processo in processos:
        if(processo.tempo_de_inicializacao > tempo_de_inicializacao_anterior):
            time.sleep(processo.tempo_de_inicializacao - tempo_de_inicializacao_anterior)
            fila.insere_processo(processo)
            #print('Processo iniciado no tempo ' + str(processo.tempo_de_inicializacao))
            tempo_de_inicializacao_anterior = processo.tempo_de_inicializacao
        else:
            fila.insere_processo(processo)
            #print('Processo iniciado no tempo ' + str(processo.tempo_de_inicializacao))

def gerencia_processos(fila_pronto, processos, recursos, memoria, disco):
    CPU = threading.Lock()
    threads = []
    processos_finalizados = []
    despachante = Despachante()
    while(len(threads) < len(processos)):
        processo = fila_pronto.remove_processo()
        if processo:
            if processo.prioridade:
                if processo.numero_instrucao == 1:
                    memoria.aloca_processo_usuario(processo)
                    despachante.despacha_processo(processo, CPU)
                    threads.append(threading.Thread(target=executa_processo, args=(processo, recursos, CPU, )))
                    threads[processo.PID].start()
                else:
                    threads[processo.PID].run()
            elif processo.prioridade == 0:
                memoria.aloca_processo_nucleo(processo)
                despachante.despacha_processo(processo, CPU)
                threads.append(threading.Thread(target=executa_processo, args=(processo, recursos, CPU, )))
                threads[processo.PID].start()
                processos_finalizados.append(1)

    for thread in threads:
        thread.join()
    despachante.executa_sistema_de_arquivos(disco)

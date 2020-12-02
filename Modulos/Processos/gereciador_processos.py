import threading
import time
import operator
from thread_processo import executa_processo 

def inicia_processos(processos, fila):
    processos = sorted(processos, key=operator.attrgetter('tempo_de_inicializacao'))
    tempo_de_inicializacao_anterior = 1
    for processo in processos:
        if(processo.tempo_de_inicializacao > tempo_de_inicializacao_anterior):
            time.sleep(processo.tempo_de_inicializacao - tempo_de_inicializacao_anterior)
            fila.insere_processo(processo)
            print('Processo iniciado no tempo ' + str(processo.tempo_de_inicializacao))
            tempo_de_inicializacao_anterior = processo.tempo_de_inicializacao
        else:
            fila.insere_processo(processo)
            print('Processo iniciado no tempo ' + str(processo.tempo_de_inicializacao))

def gerencia_processos(fila, processos, recursos, memoria, disco):
    while(true):
        processo = fila.remove_processo()
        if processo:
            #dispatcher
            

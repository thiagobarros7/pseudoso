import threading
import time
import operator

def inicia_processos(processos, fila):
    processos = sorted(processos, key=operator.attrgetter('tempo_de_inicializacao'))
    tempo_de_inicializacao_anterior = 1
    for processo in processos:
        if(processo.tempo_de_inicializacao > tempo_de_inicializacao_anterior):
            time.sleep(processo.tempo_de_inicializacao - tempo_de_inicializacao_anterior)
            print('Processo iniciado no tempo ' + str(processo.tempo_de_inicializacao))
            fila.insere_processo(processo)
            tempo_de_inicializacao_anterior = processo.tempo_de_inicializacao
        else:
            print('Processo iniciado no tempo ' + str(processo.tempo_de_inicializacao))
            fila.insere_processo(processo)

def gerencia_processos(processos):
    PID = 1
    for processo in processos:
        
        PID += 1

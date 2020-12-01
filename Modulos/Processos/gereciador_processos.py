import threading
import time
import operator

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

def gerencia_processos(processos):
    PID = 0
    for processo in processos:
        
        PID += 1

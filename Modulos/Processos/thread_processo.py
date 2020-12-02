import time
import threading

def executa_processo(processo, recursos, fila_pronto, fila_bloqueio):
    if processo.prioridade:
        if processo.numero_instrucao == 1:
            print("P"+str(processo.PID)+" STARTED")
            if recursos.requisita_recurso(processo, fila_pronto, fila_bloqueio):
                print("P"+str(processo.PID)+" instruction "+str(processo.numero_instrucao))
                if processo.numero_instrucao < processo.tempo_de_processador:
                    processo.numero_instrucao += 1
        elif processo.numero_instrucao == processo.tempo_de_processador:
            print("P"+str(processo.PID)+" instruction "+str(processo.numero_instrucao))
            recursos.desaloca_recurso(processo.recursos)
            print("P"+str(processo.PID)+" return SIGINT")
        else:
            print("P"+str(processo.PID)+" instruction "+str(processo.numero_instrucao))
            processo.numero_instrucao += 1
        time.sleep(1)
    else:
        print("P"+str(processo.PID)+" STARTED")
        for i in range(1, processo.tempo_de_processador+1):
            print("P"+str(processo.PID)+" instruction "+str(processo.numero_instrucao))
            processo.numero_instrucao += 1
            time.sleep(1)
        print("P"+str(processo.PID)+" return SIGINT")



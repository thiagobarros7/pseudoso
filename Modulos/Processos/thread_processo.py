import time
import threading

def executa_processo(processo, recursos, CPU):
    if processo.prioridade:
        flag_primeira_vez = 1
        for i in range(1, processo.tempo_de_processador+1):
            if flag_primeira_vez:
                recursos.requisita_recurso(processo)
                print("P"+str(processo.PID)+" STARTED")
                flag_primeira_vez = 0
            CPU.acquire()
            print("P"+str(processo.PID)+" instruction "+str(processo.numero_instrucao))
            processo.numero_instrucao += 1
            CPU.release()
            time.sleep(1)
        recursos.desaloca_recurso(processo)
        print("P"+str(processo.PID)+" return SIGINT")
    else:
        CPU.acquire()
        print("P"+str(processo.PID)+" STARTED")
        for i in range(1, processo.tempo_de_processador+1):
            print("P"+str(processo.PID)+" instruction "+str(processo.numero_instrucao))
            processo.numero_instrucao += 1
            time.sleep(1)
        print("P"+str(processo.PID)+" return SIGINT")
        CPU.release()

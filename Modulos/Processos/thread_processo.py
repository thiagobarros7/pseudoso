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
    #    if processo.numero_instrucao == 1:
    #        print("P"+str(processo.PID)+" STARTED")
    #        if recursos.requisita_recurso(processo, fila_pronto, fila_bloqueio):
    #            print("P"+str(processo.PID)+" instruction "+str(processo.numero_instrucao))
    #            if processo.numero_instrucao < processo.tempo_de_processador:
    #                processo.numero_instrucao += 1
    #    elif processo.numero_instrucao == processo.tempo_de_processador:
    #        print("P"+str(processo.PID)+" instruction "+str(processo.numero_instrucao))
    #        recursos.desaloca_recurso(processo.recursos)
    #        print("P"+str(processo.PID)+" return SIGINT")
    #    else:
    #        print("P"+str(processo.PID)+" instruction "+str(processo.numero_instrucao))
    #        processo.numero_instrucao += 1
    else:
        CPU.acquire()
        print("P"+str(processo.PID)+" STARTED")
        for i in range(1, processo.tempo_de_processador+1):
            print("P"+str(processo.PID)+" instruction "+str(processo.numero_instrucao))
            processo.numero_instrucao += 1
            time.sleep(1)
        print("P"+str(processo.PID)+" return SIGINT")
        CPU.release()



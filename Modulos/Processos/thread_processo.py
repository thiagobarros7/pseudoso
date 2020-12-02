import time

def executa_processo(processo, recursos):
    print("P"+str(processo.PID)+" STARTED")
    recursos.requisita_recurso(processo.recursos)
    for i in range(1, processo.tempo_de_processador+1):
        print("P"+str(processo.PID)+" instruction "+str(i))
        time.sleep(1)
    recursos.desaloca_recurso(processo.recursos)
    print("P"+str(processo.PID)+" return SIGINT")

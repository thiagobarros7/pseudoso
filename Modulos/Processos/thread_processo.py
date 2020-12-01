import time

def executa_processo(processo):
    print("P"+str(processo.PID)+" STARTED")
    for i in range(1, processo.tempo_de_processador):
        print("P"+str(processo.PID)+" instruction "+str(i))
        
        time.sleep(1)

    print("P"+str(processo.PID)+" return SIGINT")
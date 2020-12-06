import threading

class Recursos:

    def __init__(self):
        self.scanner = threading.Lock()
        self.modem = threading.Lock()
        self.impressora = threading.Semaphore(2)
        self.sata = threading.Semaphore(2)
    
    def requisita_recurso(self, processo):
        for recurso, requisicao in enumerate(processo.recursos):
            utilizando = processo.recursos[requisicao]
            if utilizando:
                if requisicao == 'cod_impressora':
                    print('P' + str(processo.PID) + ' esperando por recurso: ' + requisicao)
                    self.impressora.acquire()
                    print('P' + str(processo.PID) + ' lockando recurso: ' + requisicao)
                    return()
                elif requisicao == 'scanner':
                    print('P' + str(processo.PID) + ' esperando por recurso: ' + requisicao)
                    self.scanner.acquire()
                    print('P' + str(processo.PID) + ' lockando recurso: ' + requisicao)
                    return()
                elif requisicao == 'modem':
                    print('P' + str(processo.PID) + ' esperando por recurso: ' + requisicao)
                    self.modem.acquire()
                    print('P' + str(processo.PID) + ' lockando recurso: ' + requisicao)
                    return()
                elif requisicao == 'cod_disco':
                    print('P' + str(processo.PID) + ' esperando por recurso: ' + requisicao)
                    self.sata.acquire()
                    print('P' + str(processo.PID) + ' lockando recurso: ' + requisicao)
                    return()

    def desaloca_recurso(self, processo):
        for recurso, requisicao in enumerate(processo.recursos):
            utilizando = processo.recursos[requisicao]
            if utilizando:
                if requisicao == 'cod_impressora':
                    print('P' + str(processo.PID) + ' desalocando recurso: ' + requisicao)
                    self.impressora.release()
                elif requisicao == 'scanner':
                    print('P' + str(processo.PID) + ' desalocando recurso: ' + requisicao)
                    self.scanner.release()
                elif requisicao == 'modem':
                    print('P' + str(processo.PID) + ' desalocando recurso: ' + requisicao)
                    self.modem.release()
                elif requisicao == 'cod_disco':
                    print('P' + str(processo.PID) + ' desalocando recurso: ' + requisicao)
                    self.sata.release()

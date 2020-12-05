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
                    self.impressora.acquire()
                    print('lockando recurso: '+ requisicao)
                    return()
                elif requisicao == 'scanner':
                    self.scanner.acquire()
                    print('lockando recurso: '+ requisicao)
                    return()
                elif requisicao == 'modem':
                    self.modem.acquire()
                    print('lockando recurso: '+ requisicao)
                    return()
                elif requisicao == 'cod_disco':
                    self.sata.acquire()
                    print('lockando recurso: '+ requisicao)
                    return()

    def desaloca_recurso(self, processo):
        for recurso, requisicao in enumerate(processo.recursos):
            utilizando = processo.recursos[requisicao]
            if utilizando:
                if requisicao == 'cod_impressora':
                    print('desalocando recurso: '+ requisicao)
                    self.impressora.release()
                elif requisicao == 'scanner':
                    print('desalocando recurso: '+ requisicao)
                    self.scanner.release()
                elif requisicao == 'modem':
                    print('desalocando recurso: '+ requisicao)
                    self.modem.release()
                elif requisicao == 'cod_disco':
                    print('desalocando recurso: '+ requisicao)
                    self.sata.release()

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
                    print('lockando recurso: '+ requisicao)
                    self.impressora.acquire()
                    return()
                elif requisicao == 'scanner':
                    print('lockando recurso: '+ requisicao)
                    self.scanner.acquire()
                    return()
                elif requisicao == 'modem':
                    print('lockando recurso: '+ requisicao)
                    self.modem.acquire()
                    return()
                elif requisicao == 'cod_disco':
                    print('lockando recurso: '+ requisicao)
                    self.sata.acquire()
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

import threading

class Recursos:

    def __init__(self):
        self.scanner = threading.Semaphore()
        self.modem = threading.Semaphore()
        self.impressora = threading.Semaphore(2)
        self.sata = threading.Semaphore(2)
    
    def requisita_recurso(self, recursos_processo):
        for recurso, requisicao in enumerate(recursos_processo):
            if requisicao:
                if recurso == 'cod_impressora':
                    self.impressora.acquire()
                elif recurso == 'scanner':
                    self.scanner.acquire()
                elif recurso == 'modem':
                    self.modem.acquire()
                elif recurso == 'cod_disco':
                    self.sata.acquire()

    def desaloca_recurso(self, recursos_processo):
        for recurso, requisicao in enumerate(recursos_processo):
            if requisicao:
                if recurso == 'cod_impressora':
                    self.impressora.release()
                elif recurso == 'scanner':
                    self.scanner.release()
                elif recurso == 'modem':
                    self.modem.release()
                elif recurso == 'cod_disco':
                    self.sata.release()

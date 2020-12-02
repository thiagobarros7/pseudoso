import threading

class Recursos:

    def __init__(self):
        self.scanner = 1
        self.modem = 1
        self.impressora = 2
        self.sata = 2
    
    def requisita_recurso(self, processo, fila_pronto, fila_bloqueio):
        for recurso, requisicao in enumerate(processo.recursos):
            if requisicao:
                if recurso == 'cod_impressora':
                    if self.impressora - 1 >= 0:
                        self.impressora -= 1
                        return(1)
                    else:
                        fila_bloqueio.insere_na_fila('impressora', processo)
                        return(0)
                elif recurso == 'scanner':
                    if self.scanner - 1 >= 0:
                        self.scanner -= 1
                        return(1)
                    else:
                        fila_bloqueio.insere_na_fila('scanner', processo)
                        return(0)
                elif recurso == 'modem':
                    if self.modem - 1 >= 0:
                        self.modem -= 1
                        return(1)
                    else:
                        fila_bloqueio.insere_na_fila('modem', processo)
                        return(0)
                elif recurso == 'cod_disco':
                    if self.sata - 1 >= 0:
                        self.sata -= 1
                        return(1)
                    else:
                        fila_bloqueio.insere_na_fila('sata', processo)
                        return(0)
        return(1)

    def desaloca_recurso(self, recursos_processo):
        for recurso, requisicao in enumerate(recursos_processo):
            if requisicao:
                if recurso == 'cod_impressora':
                    self.impressora += 1
                    if fila_bloqueio.remove_da_fila('impressora', fila_pronto):
                        return(1)
                    else:
                        return(0)
                elif recurso == 'scanner':
                    self.scanner += 1
                    if fila_bloqueio.remove_da_fila('scanner', fila_pronto):
                        return(1)
                    else:
                        return(0)
                elif recurso == 'modem':
                    self.modem += 1
                    if fila_bloqueio.remove_da_fila('modem', fila_pronto):
                        return(1)
                    else:
                        return(0)
                elif recurso == 'cod_disco':
                    self.sata += 1
                    if fila_bloqueio.remove_da_fila('sata', fila_pronto):
                        return(1)
                    else:
                        return(0)
        return(1)

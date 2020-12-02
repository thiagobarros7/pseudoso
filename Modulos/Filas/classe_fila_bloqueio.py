class FilaBloqueio():
    def __init__(self):
        self.fila = {'impressora': [], 'scanner': [], 'sata': [], 'modem': []}

    def insere_na_fila(self, recurso, processo):
        self.fila[recurso].append(processo)
        return(1)
    
    def remove_da_fila(self, recurso, fila_pronto):
        if self.fila[recurso] is not None:
            processo = self.fila[recurso].pop()
            fila_pronto.insere_ṕrocesso(processo)
            return(1)
        return(0)

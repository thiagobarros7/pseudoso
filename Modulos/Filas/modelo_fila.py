class Fila:
    def __init__(self):
        self.prioridade1 = []
        self.prioridade2 = []
        self.prioridade3 = []
        self.fila_tempo_real = []
        self.fila_usuario = {"prioridade1": self.prioridade1, "prioridade2": self.prioridade2, "prioridade3": self.prioridade3}

    def insere_processo(self, processo):
        if((processo.prioridade == 0) and (len(self.fila_tempo_real) <= 1000)):
            fila_tempo_real.append(processo)
        elif((processo.prioridade == 1) and (len(self.fila_usuario["prioridade1"]) <= 1000)):
            fila_usuario["prioridade1"].append(processo)
        elif((processo.prioridade == 2) and (len(self.fila_usuario["prioridade2"]) <= 1000)):
            fila_usuario["prioridade2"].append(processo)
        elif((processo.prioridade == 3) and (len(self.fila_usuario["prioridade3"]) <= 1000)):
            fila_usuario["prioridade3"].append(processo)
        else:
            print("Não há espaço na fila.")
            return(0)
        return(1)
    
    def atualiza_prioridades(self):
        self.fila_usuario['prioridade1'].extend(self.fila_usuario['prioridade2'])
        self.fila_usuario['prioridade2'] = self.fila_usuario['prioridade3']
        self.fila_usuario['prioridade3'] = []

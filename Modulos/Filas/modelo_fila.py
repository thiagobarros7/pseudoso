class Fila:
    def __init__(self):
        self.prioridade1 = []
        self.prioridade2 = []
        self.prioridade3 = []
        self.fila_tempo_real = []
        self.fila_usuario = {"prioridade1": self.prioridade1, "prioridade2": self.prioridade2, "prioridade3": self.prioridade3}

    def insere_processo(self, processo):
        if((processo.prioridade == 0) and (len(self.fila_tempo_real) <= 1000)):
            self.fila_tempo_real.append(processo)
        elif((processo.prioridade == 1) and (len(self.fila_usuario["prioridade1"]) <= 1000)):
            self.fila_usuario["prioridade1"].append(processo)
        elif((processo.prioridade == 2) and (len(self.fila_usuario["prioridade2"]) <= 1000)):
            self.fila_usuario["prioridade2"].append(processo)
        elif((processo.prioridade == 3) and (len(self.fila_usuario["prioridade3"]) <= 1000)):
            self.fila_usuario["prioridade3"].append(processo)
        else:
            print("Não há espaço na fila.")
            return(0)
        return(1)
    
    def __atualiza_prioridades(self):
        self.fila_usuario['prioridade1'].extend(self.fila_usuario['prioridade2'])
        self.fila_usuario['prioridade2'] = self.fila_usuario['prioridade3']
        self.fila_usuario['prioridade3'] = []

    def remove_processo(self):
        if(len(self.fila_tempo_real) > 0):
            processo = self.fila_tempo_real.pop(0)
            self.__atualiza_prioridades()
            return(processo)
        elif(len(self.fila_usuario['prioridade1']) > 0):
            processo = self.fila_usuario['prioridade1'].pop(0)
            self.__atualiza_prioridades()
            return(processo)
        elif(len(self.fila_usuario['prioridade2']) > 0):
            processo = self.fila_usuario['prioridade2'].pop(0)
            self.__atualiza_prioridades()
            return(processo)
        elif(len(self.fila_usuario['prioridade3']) > 0):
            processo = self.fila_usuario['prioridade3'].pop(0)
            self.__atualiza_prioridades()
            return(processo)
        else:
            print('Não há processos na fila.')
            return(0)

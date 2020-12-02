class Memoria:
    def __init__(self, tamanho_memoria):
        self.memoria = [0]*tamanho_memoria
        self.offset_usuario = 64
        self.offset_nucleo = 0

    def __verifica_memoria(self, offset, tamanho_processo, nucleo=0):
        if(nucleo and (tamanho_processo+offset >= 64)):
            return(0)
        elif(tamanho_processo+offset >= len(self.memoria)):
            return(0)
        else:
            for index in range(offset, tamanho_processo+offset):
                if self.memoria[index] != 0:
                    return(0)
        return(1)
    
    def __aloca_processo(self, offset, tamanho_processo, PID):
        for index in range(offset, tamanho_processo+offset):
            self.memoria[index] = PID

    def aloca_processo_usuario(self, processo):
        if self.__verifica_memoria(self.offset_usuario, processo.blocos_em_memoria):
            self.__aloca_processo(self.offset_usuario, processo.blocos_em_memoria, processo.PID)
            processo.offset = self.offset_usuario
            self.offset_usuario = self.offset_usuario+processo.blocos_em_memoria
        else:
            print('Não foi possivel alocar o processo em memória')
            return(0)
        return(1)

    def aloca_processo_nucleo(self, processo):
        if self.__verifica_memoria(self.offset_nucleo, processo.blocos_em_memoria, 1):
            self.__aloca_processo(self.offset_nucleo, processo.blocos_em_memoria, processo.PID)
            processo.offset = self.offset_nucleo
            self.offset_nucleo = self.offset_nucleo+processo.blocos_em_memoria
        else:
            print('Não foi possivel alocar o processo em memória')
            return(0)
        return(1)

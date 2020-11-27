class Memoria:
    def __init__(self, tamanho_memoria):
        self.memoria = [0]*tamanho_memoria
        self.offset_usuario = 64
        self.offset_nucleo = 0

    def __verifica_memoria(self, offset, tamanho_processo, nucleo=0):
        if(nucleo and (tamanho_processo+offset >= 64)):
            return(0)
        elif(tamanho_processo+offset >= self.tamanho_memoria):
            return(0)
        else:
            for index in range(offset, tamanho_processo+offset):
                if self.memoria[index] != 0:
                    return(0)
        return(1)
    
    def __aloca_processo(self, offset, tamanho_processo, PID):
        for index in range(offset, tamanho_processo+offset):
            self.memoria[index] = PID

    def aloca_processo_usuario(self, tamanho_processo, PID):
        if self.__verifica_memoria(self.offset_usuario, tamanho_processo):
            self.__aloca_processo(self.offset_usuario, tamanho_processo, PID)
            self.offset_usuario = self.offset_usuario+tamanho_processo
        else:
            print('Não foi possivel alocar o processo em memória')
            return(0)
        return(1)

    def aloca_processo_nucleo(self, tamanho_processo, PID):
        if self.__verifica_memoria(self.offset_nucleo, tamanho_processo, 1):
            self.__aloca_processo(self.offset_nucleo, tamanho_processo, PID)
            self.offset_nucleo = self.offset_nucleo+tamanho_processo
        else:
            print('Não foi possivel alocar o processo em memória')
            return(0)
        return(1)

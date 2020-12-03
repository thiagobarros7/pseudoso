import threading

class Memoria:
    def __init__(self, tamanho_memoria):
        self.memoria = [0]*tamanho_memoria
        self.offset_usuario = 64
        self.offset_nucleo = 0
        self.controle_memoria = threading.Lock()
        self.memoria_usuario_cheia = threading.Lock()
        self.memoria_nucleo_cheia = threading.Lock()
        self.memoria_nucleo_cheia.acquire()
        self.memoria_usuario_cheia.acquire()

    def __verifica_memoria(self, offset, tamanho_processo, nucleo=0):
        if(nucleo and (tamanho_processo > 64)):
            return(0)
        elif(tamanho_processo+offset > len(self.memoria)):
            return(0)
        else:
            for index in range(offset, tamanho_processo+offset):
                if self.memoria[index] != 0:
                    if nucleo:
                        self.memoria_nucleo_cheia.acquire()
                    else:
                        self.memoria_usuario_cheia.acquire()
                    return(1)
        return(1)
    
    def __aloca_processo(self, offset, tamanho_processo, PID):
        for index in range(offset, tamanho_processo+offset):
            self.memoria[index] = PID

    def aloca_processo_usuario(self, processo):
        self.controle_memoria.acquire()
        if self.__verifica_memoria(self.offset_usuario, processo.blocos_em_memoria):
            self.__aloca_processo(self.offset_usuario, processo.blocos_em_memoria, processo.PID)
            processo.offset = self.offset_usuario
            self.offset_usuario = self.offset_usuario+processo.blocos_em_memoria
        else:
            print('Não foi possivel alocar o processo ' + processo.PID + ' em memória')
            self.controle_memoria.release()
            return(0)
        self.controle_memoria.release()
        return(1)

    def aloca_processo_nucleo(self, processo):
        self.controle_memoria.acquire()
        if self.__verifica_memoria(self.offset_nucleo, processo.blocos_em_memoria, 1):
            self.__aloca_processo(self.offset_nucleo, processo.blocos_em_memoria, processo.PID)
            processo.offset = self.offset_nucleo
            self.offset_nucleo = self.offset_nucleo+processo.blocos_em_memoria
        else:
            print('Não foi possivel alocar o processo em memória')
            self.controle_memoria.release()
            return(0)
        self.controle_memoria.release()
        return(1)

    def desaloca_processo_usuario(self, processo):
        self.controle_memoria.acquire()
        for index, espaco in enumerate(self.memoria):
            if espaco == processo.PID:
                self.memoria[index] = 0
        if self.memoria_usuario_cheia.locked():
            self.memoria_usuario_cheia.release()
        self.controle_memoria.release()


    def desaloca_processo_nucleo(self, processo):
        self.controle_memoria.acquire()
        for index, espaco in enumerate(self.memoria):
            if espaco == processo.PID:
                self.memoria[index] = 0
        if self.memoria_nucleo_cheia.locked():
            self.memoria_nucleo_cheia.release()
        self.controle_memoria.release()

from Modulos.Interface.entrada import le_arquivos, le_processos
from Modulos.Filas.modelo_fila import Fila
from Modulos.Memoria.modelo_memoria import Memoria
from Modulos.Processos.modelo_processo import Processo
from Modulos.Processos.gereciador_processos import inicia_processos

import threading

print('Inicializando Pseudo-SO')
print('Alocando memória principal')
memoria = Memoria(1024)
print('Criando fila de pronto')
fila_pronto = Fila()
print('Lendo os processos')
processos = le_processos()
print('Iniciando Processos')
inicia_processos = threading.Thread(target=inicia_processos(processos, fila_pronto), args=())
inicia_processos.start()

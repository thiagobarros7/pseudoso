from Modulos.Interface.entrada import le_arquivos, le_processos
from Modulos.Interface.dispatcher import Despachante
from Modulos.Arquivos.classe_disco import Disco
from Modulos.Recursos.classe_recursos import Recursos
from Modulos.Filas.modelo_fila import Fila
from Modulos.Filas.classe_fila_bloqueio import FilaBloqueio
from Modulos.Memoria.modelo_memoria import Memoria
from Modulos.Processos.modelo_processo import Processo
from Modulos.Processos.gereciador_processos import inicia_processos, gerencia_processos

import threading

print('Inicializando Pseudo-SO')
print('Lendo os processos')
processos = le_processos()
print('Lendo os arquivos')
arquivos = le_arquivos()
print('Alocando memória principal')
memoria = Memoria(1024)
print('Criando disco com seus arquivos iniciais')
disco = Disco(arquivos)
print('Reconhecendo os recursos disponiveis(dispositivos)')
recursos = Recursos()
print('Criando fila de pronto')
fila_pronto = Fila()
print('Criando fila de bloqueio')
fila_bloqueio = FilaBloqueio()
print('Iniciando Processos')
inicia_processos = threading.Thread(target=inicia_processos, args=(processos, fila_pronto, ))
inicia_processos.start()
('Iniciando gerenciador de Processos')
gerencia_processos(fila_pronto, fila_bloqueio, processos, recursos, memoria, disco)

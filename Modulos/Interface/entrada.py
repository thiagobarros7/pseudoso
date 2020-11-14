def le_processos():
	from pathlib import Path
	from Modulos.Processos.modelo_processo import Processo

	processos_objeto = []

	path = Path(__file__).parent / "../../Arquivos/processes.txt"
	with path.open() as arquivo:
		for processo in arquivo:
			processos_objeto.append(Processo(processo.split(',')))
	return(processos_objeto)
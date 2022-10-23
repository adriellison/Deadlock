# Bibliotecas

# Funções
from configs.simple import *

# Acessando módulos
import impasses

def entrarMenu():
	try:
		cls()
		print('''\n
		+-----------------------------------------------------------------------+
		|                            TELA DE INICIO                             |
		|-----------------------------------------------------------------------|
		|  1 = Verificar arquivo                                                |
		|-----------------------------------------------------------------------|
		|  2 =                                                                  |
		|-----------------------------------------------------------------------|
		|                               0 = Sair                                |
		+-----------------------------------------------------------------------+\n
	''')
		opcao = int(input('\t>:  '))
		if opcao == 1:
			impasses.verificarArquivo()
			entrarMenu()
		elif opcao == 2:
			not_in()
			entrarMenu()
		elif opcao == 3:
			not_in()
			entrarMenu()
		elif opcao == 0:
			finalizar()
		else:
			cls()
			invalida()
	except:
		entrarMenu()

entrarMenu()

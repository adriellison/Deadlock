# Funções
from configs.simple import *

def verificarArquivo():
	try:
		file = open('entrada.txt', 'r')
		saida = file.read()
		file.close()
		print(saida)
	except IOError as e:
		print('O arquivo não pode ser aberto.\nPor favor, verifique se o arquivo existe e está fechado.')
	press()

def lerArquivo():
	file = open('entrada.txt', 'r')
	saida = file.read()
	file.close()
	print(saida)
	press()
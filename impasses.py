# Funções
from concurrent.futures import process
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

def verificaRecursos():
	file = open('entrada.txt', 'r')
	linha = file.readline()
	file.close()
	lista = linha.split(" ")
	return lista

def imprimeRecursos():
	print(f"Números de processos: {verificaRecursos()[0]}")
	print(f"Número de recursos: {verificaRecursos()[1]}")
	
def allFile():
	file = open('entrada.txt', 'r')
	linhas = file.readlines()
	file.close()
	return linhas

def verificarLinhas():
	processos = int(verificaRecursos()[0])
	recursos = int(verificaRecursos()[1])

	print(f"Números de processos: {verificaRecursos()[0]}")
	print(f"Número de recursos: {verificaRecursos()[1]}")
	
	linhas = allFile()
	linhas = [ x for x in linhas if x != '\n' ]
	# print(linhas)
	# matriz1 = linhas[3]
	# print(linhas[3])
	primeiroArray = 3
	segundoArray = primeiroArray + processos
	print(linhas[primeiroArray])
	print(linhas[segundoArray])
	
	for j in linhas


verificarLinhas()
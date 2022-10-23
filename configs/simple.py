import os
import time

def cls():
	os.system('cls')

def carregar():
	lista = [
	'▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒0%',
	'█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒5%',
	'███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒15%',
	'█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒25%',
	'███████▒▒▒▒▒▒▒▒▒▒▒▒▒35%',
	'█████████▒▒▒▒▒▒▒▒▒▒▒45%',
	'███████████▒▒▒▒▒▒▒▒▒55%',
	'█████████████▒▒▒▒▒▒▒65%',
	'███████████████▒▒▒▒▒75%',
    '█████████████████▒▒▒85%',
	'███████████████████▒95%',
	'████████████████████100%']
	for i in lista:
		time.sleep(0.05),cls(),print('\n\n\n\n\n\n\n\t\t\t\tCarrengando sistema...\n\t\t\t\t',i)
	cls()

def espaco():
	print("\n" * 5)

def not_in():
	print('\n\tAinda não implementado')

def press():
	input('\n\t\tPressione qualquer tecla para continuar!\n')

def invalida():
	print('\n\tOpção inválida!')

def vazio():
	cls()
	print("\n\tO campo não pode ficar em branco!\n")

def finalizar():
	cls()
	# print('\n\tFinalizando sistema!')
	lista = [
	'▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒0%',
	'████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒20%',
	'████████▒▒▒▒▒▒▒▒▒▒▒▒40%',
	'████████████▒▒▒▒▒▒▒▒60%',
	'████████████████▒▒▒▒80%',
	'████████████████████100%']
	for i in lista:	
		time.sleep(0.05),cls(),print('\n\n\n\n\n\n\n\t\t\t\tFinalizando sistema...\n\t\t\t\t',i)
	os.system('taskkill /F /IM cmd.exe')
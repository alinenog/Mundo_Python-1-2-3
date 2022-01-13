#Exercício Python 32:,
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

'''
ano=int(input('Digite o ano que deseja saber se é BISSEXTO: '))
if ano % 4  == 0 and ano % 100 != 0 or ano % 400 == 0:
  print(f'{ano} é um ano BISSEXTO!')
else:
  print(f'{ano} não é um ano BISSEXTO!')  
'''  

from datetime import date
ano = int(input('Digite o ano que deseja analisar: '))
if ano == 0: # se igual a 0 ele analisara, o ano da maquina que o programa esta rodando
  ano = date.today().year
if ano % 4  == 0 and ano % 100 != 0 or ano % 400 == 0:
  print(f'{ano} é um ano BISSEXTO!')
else:
  print(f'{ano} não é um ano BISSEXTO!')
  
  
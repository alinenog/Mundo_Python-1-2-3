# 16)Exercício Python 16:
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

''' IMPORTANDO MODULO
from math import trunc
num = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porção inteira é {}' .format(num, trunc(num)))
'''

#SEM IMPORATAR MODULO
#Recebe o número em float e tranforma para inteiro
num = float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porcao inteira é {}'.format(num, int(num)))




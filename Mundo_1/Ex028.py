#Exercício Python 28:
# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o #usuário tentar descobrir qual foi o número
# escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep #Faz o computador dormi

print('=-'*15)
print('       TENTE ADIVINHAR!   ')
print('=-'*15)
computador = randint(0, 5) #Vai gerar o número que o computador pesnsou
print('Vou pensar em um número de 0 a 5 tente adivinhar: ')
num = int(input('Em que número eu pensei? '))
print('Penssando ...')
sleep(3)
if num != computador:
  print(f'Você errou e eu ganhei! Eu pensei no numero {computador} mas você pensou no número {num}!')
else:
  print(f'Parabéns você venceu!Eu pensei no número {computador} e você também pensou no número {num}!')  
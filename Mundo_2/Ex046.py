#Exercício Python 46:
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos #de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles

"""
from time import sleep
print('''FOGOS DE ARTIFÍCIL
Digite a opção
[ 1 ] para acender
[ 2 ] Para explodir na sua mão (não recomendado)''')
opção = int(input('Digite a opção: '))
if opção == 1:
    for c in range(10, -1, -1):
        sleep(1)
        print(c)
    print('BOOOOOOM!!!')
elif opção == 2:
    sleep(1)
    print('BOOOOOOM!!!')
    print('Sua mão ainda está ai? kkk')
else:
    print('Opção invalida! acenda novamente :)')
"""
from time import sleep
for c in range(10, -1, -1):
  print(c)
  sleep(1)
print('* Fogos Artificios * ')

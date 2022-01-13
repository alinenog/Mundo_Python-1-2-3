#Exercício Python 35:
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não #formar um triângulo

print('=-'*20)
print('        AnaLisAdoR de TRianGuLo   ')
print('=-'*20)
primeiro = float(input('Digite o primeiro seguimento: '))
segundo = float(input('Digite o segundo seguimento: '))
terceiro = float(input('Digite o terceiro seguimento: '))
#Cada um dos seguimentos tem que ser menor que a soma dos outros dois
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
  print('Esses segmentos podem formar um TRIANGULO!')
else:
  print('Esses segmentos não podem formar um TRIANGULO!')
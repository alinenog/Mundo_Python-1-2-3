#Exercício Python 42:
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de 
# #triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

print('=-'*20)
print('        AnaLisAdoR de TRianGuLo   ')
print('=-'*20)
primeiro = float(input('Digite o primeiro seguimento: '))
segundo = float(input('Digite o segundo seguimento: '))
terceiro = float(input('Digite o terceiro seguimento: '))
#Cada um dos seguimentos tem que ser menor que a soma dos outros dois
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
  print('Esses segmentos podem formar um TRIANGULO.')
  
  #– EQUILÁTERO: todos os lados iguais
  if primeiro == segundo == terceiro:
    print('Pode formar um triângulo: EQUILÁTERO!')
  #– ESCALENO: todos os lados diferentes
  elif primeiro != segundo != terceiro != primeiro:
    print('Pode formar um triângulo ESCALENO!')
  #– ISÓSCELES: dois lados iguais, um diferente
  else:
    print('Pode formar um triângulo: ISÓSCELES!')
else:
  print('Esses segmentos não podem formar um TRIANGULO!')
  
  
  
  
  
'''
print('Pode formar um triângulo: EQUILÁTERO')
elif:
print('Pode formar um triângulo: ISÓSCELES')
else:
print('Pode formar um triângulo ESCALENO')
'''

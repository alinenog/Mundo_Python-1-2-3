#Exercício Python 47: 
# Crie um programa que mostre na tela todos os números pares que estão no intervalo #entre 1 e 50.

'''
# Nesse exemplo faz menas interação, gastando menos processador
for num in range(2, 51, 2):
  print('.', end='') 
  print(num, end=' ')
print('\nAcabou!!!')
'''

# Nesse exemplo faz mais interação, gastando mais processador
for num in range(1, 50):
  print('.', end='')
  if num % 2 == 0:
    print(num, end=' ')
print('\nAcabou!!!')   

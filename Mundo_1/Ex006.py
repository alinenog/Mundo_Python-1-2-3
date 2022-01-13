#Exercício Python 006:
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

''' Outro modo de fazer o algoritimo
num = int(input('Digite um número: '))
dobro = num * 2
triplo=num * 3
raiz = num ** (1/2)
print(f'O dobro de {num} é {dobro}.')
print(f'O triplo de {num} é {triplo}.')
print(f'A raiz quadrada de {num} é {raiz}.')'''

import math
num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = math.sqrt(num)
print(f'O dobro de {num} é {dobro}')
print(f'O triplo de {num} é {triplo}')
print(f'A raiz quadrada de {num} é {raiz}')
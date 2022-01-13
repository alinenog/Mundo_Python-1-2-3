# Exercício Python 18:
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse #ângulo.
'''
from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))

#converti o angulo em radiano, de radiano para seno
seno = sin(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')

#converti o angulo em radiano, de radiano para cosseno
cosseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')

#converti o angulo em radiano, de radiano para tangente
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')'''

import math
angulo = float(input('Digite o ângulo que você deseja: '))

#Foi convertido o angulo em radiano, de radiano para seno
seno = math.sin(math.radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')

#Foi convertido o angulo em radiano, de radiano para cosseno
cosseno = math.cos(math.radians(angulo))
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')

#Foi convertido o angulo em radiano, de radiano para tangente
tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')


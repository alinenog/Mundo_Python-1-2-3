#Exercício Python 55:
# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for p in range(1,6):
  peso = float(input(f'Peso da {p}ª pessoa: Kg '))
  #maior e menor peso para a ser o primeiri numero recebido
  if p == 1:
    maior = peso
    menor = peso
  else:
      if peso > maior:
          maior = peso
      if peso < menor:
        menor = peso     
print(f'\nO maior peso lido foi {maior} kg')
print(f'O menor peso lido foi {menor} kg')  
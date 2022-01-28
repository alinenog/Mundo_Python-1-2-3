#Exercício Python 56:
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o 
# nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
total_mulher20 = 0

for pes in range(1,5):
  print(f'----- {pes}ª pessoa -----')
  nome = str(input('Nome: ')).strip()
  idade = int(input('Idade: '))
  sexo = str(input('Sexo [F/M]: ')).strip()
  soma_idade += idade
  #calculo homem mais velho
  if pes == 1 and sexo in 'Mm':
    maior_idade_homem = idade
    nome_velho = nome 
  if sexo in 'Mm' and idade > maior_idade_homem:
    maior_idade_homem = idade
    nome_velho = nome     
  #mulher 20
  if sexo in 'Ff' and idade < 20:  
    total_mulher20 += 1   
#calculo da média de idade
media_idade = soma_idade/4
print(f'A média de idade do grupo é {media_idade} anos.')  
print(f'O homem mais velho é {nome_velho} com {maior_idade_homem} anos de idade.')
print(f'Ao todo são {total_mulher20} mulheres com 20 anos.')
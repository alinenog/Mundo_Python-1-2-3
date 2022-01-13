#Exercício Python 041:
# A Confederação Nacional de Natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM – Até 14 anos: INFANTIL – Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR – Acima de 25 anos: MASTER

''' OUTRA FORMA DE CALCULO

from datetime import date
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Confederação Nacional de Natação')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
atual = date.today().year
nasc = int(input('Informe o ano do seu nascimento! \n'))
idade = atual - nasc
print(f'O(a) atleta tem {idade} anos!')

if idade <= 9:
  print('Categoria MIRIM!')
elif idade <= 14:
  print('Categoria INFANTIL!')
elif idade <= 19:
  print('Catgoria JUNIOR!')
elif idade <= 25:
  print('Categoria SÊNIOR!')
else:
  print('Categoria MASTER!')
'''

from datetime import date

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Confederação Nacional de Natação')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
atual = date.today().year
nasc=int(input('Informe o ano do seu nascimento! \n'))
idade = atual - nasc
print(f'O(a) atleta tem {idade} anos!')

if idade<= 9 :
  print('Categoria MIRIM!')
  
elif idade > 9 and idade <= 14:  
  print('Categoria INFANTIL!')
  
elif idade > 14 and idade <= 19:
  print('Catgoria JUNIOR!')
   
elif idade > 19 and idade <= 25:   
  print('Categoria SÊNIOR!')  
  
elif idade > 25:
  print('Categoria MASTER!')
  
else:
  print('Escolha uma categoria!')

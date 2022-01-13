#Exercício Python 37:
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário 
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número inteiro: "))
print('''Escolha a base para conversão 
      [1] Converter para BINARIO
      [2] Converter para OCTAL
      [3] Converter para HEXADECIMAL      
      ''')
opcao = int(input("Escolha uma opcao para conversão!"))
if opcao == 1:
  print('{} convertido para Binário é igual a {}.'.format(num, bin(num)[2:]))
  
elif opcao == 2:                   
  print("{} convertido para Octal é {}".format(num, oct(num)[:2]))
  
elif opcao == 3:
  print("{} convertido para Hexadecimal é {}".format(num, hex(num)[2:])) # [2:] fatiamento de string

else:
  print("Escolha a opção 1, 2 ou 3")  
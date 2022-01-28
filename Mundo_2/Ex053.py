# Exercício Python 53:
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# #desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO,
# ANOTARAM A DATA DA MARATONA.

''' #Sem usar o for
print('=-='*10)
print('     LEITOR DE PALIMDROMO ')
print('=-='*10)
# Retirando espaço e colocando tudo para maisculo
frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()  # Dividindo a frase em palavras, transformando em um vetor
junto = ''.join(palavras)  # Retirando espaços
inverso = junto[::-1]
print(f'O inverso de {frase} é | {inverso} |.')
if inverso == junto:
  print('Temos um palíndromo!')
else:
  print('A frase digitada não é um palindromo!')
'''

print('=-='*10)
print('     LEITOR DE PALIMDROMO ')
print('=-='*10)
# Retirando espaço e colocando tudo para maisculo
frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()  # Dividindo a frase em palavras, transformando em um vetor
junto = ''.join(palavras)  # Retirando espaços
inverso = '' #inverso começa vazio
for letra in range(len(junto) - 1, -1, -1):# Da ultima letra ate a primeira de um em um
    inverso += junto[letra]
print(f'O inverso de {frase} e | {inverso} |.')    
if inverso == junto:    
  print('Temos um palíndromo!')
else:
  print('A frase digitada não é um palindromo!')

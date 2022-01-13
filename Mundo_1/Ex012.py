# Exercício Python 12:
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('----------------------------')
print('      LEITOR DE PREÇO       ')
print('----------------------------')
print()
vl = float(input('Digite o valor do produto? R$'))
d = (vl * 5) /100
print('Preço do produto atual R$ {}'.format(vl))
print('|Preço do produto com 5% de desconto é R$ {:.2f}|'.format(vl-d))
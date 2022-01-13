#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10 % de desconto
#– à vista no cartão: 5 % de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20 % de juros

valorAtual= float(input('Digite o valor do produto: R$ '))
print('''\n Menu caixa 
      [1] A vista dinheiro 
      [2] A vista cheque 
      [3] Cartão credito  (a vista) 
      [4] Cartão credito  (até 2 vezes)
      [5] Cartão credito  (3 vezes ou mais)
      ''')
opcao = int(input('Escolha a forma de pagamento: '))
# à vista dinheiro: 10 % de desconto
if opcao == 1:
  novoValor = valorAtual - ((valorAtual * 10)/100)  
  print(f'Pagamento R${valorAtual} avista em dinheiro. \n O valor a ser pago é R${novoValor:.2f} com 10% de desconto.')

# cheque: 10 % de desconto
if opcao == 2:
  novoValor = valorAtual - ((valorAtual * 10)/100)
  print(
      f'Pagamento R${valorAtual} avista em cheque. \n O valor a ser pago é R${novoValor:.2f} com 10% de desconto.')
  
#– à vista no cartão: 5 % de desconto
if opcao == 3:
  novoValor = valorAtual - ((valorAtual * 5 )/100)
  print(
      f'Pagamento a vista no cartão de credito.\n O valor a pagar será R${novoValor:.2f} com 5% de desconto.')

#– em até 2x no cartão: preço formal
if opcao == 4:
  novoValor = valorAtual / 2
  print(f'Pagamento parcelado em 2 vezes. \n O valor a pagar será duas parcelas de R${novoValor:.2f}')
  
#– 3x ou mais no cartão: 20 % de juros
if opcao == 5:
  novoValor = valorAtual / 3
  print(f'Pagamento parcelado em 3 vezes. \n O valor a pagar será três parcelas de R${novoValor:.2f}')

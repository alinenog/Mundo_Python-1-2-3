#Exercício Python 36:
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da #casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30 %
#do salário ou então o empréstimo será negado.

''' Calculo menor
 quantidade_parcelas = valor_casa/(anos *12)
 porcntagem = sal *30 /100
'''

print("=-" * 18)
print("      SIMULAÇÃO DE EMPRESTIMO")
print("=-" * 18)

valor_casa = float(input("Qual o valor da casa que deseja realizar a simulação!: R$"))
sal = float(input("Qual o valor do seu salario? R$"))
anos = int(input("Em quantos anos deseja pagar sua casa: "))

#Calculo do emprestimo=================
# 30% do salario
porcentagem = (sal * 30)/100 
#Quantidade de parcelas 
quantidade_parcelas = anos * 12 
#Valor parcela
valor_parcela = valor_casa /quantidade_parcelas

if valor_parcela > porcentagem:
  print("Emprestimo Negado!")
else:
  print("Emprestimo pode ser Concedido!")
print()  
print("===== Relatório de emprestimo =====")  
print(f"Valor casa R$ {valor_casa}")  
print(f"Quantidade de parcelas {quantidade_parcelas}")
print(f"valor da parcela R${valor_parcela}")



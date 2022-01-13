#Exercício Python 29:
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem #dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

print('='*30)
print('  CONTROLE DE VELOCIDADE')
print('='*30)

velocidade = float(input('Digite a velocidade do seu carro: '))
if velocidade > 80:
  multa = (velocidade - 80) * 7  
  print('Multado! Você excedeu o limite determinado que é de 80km/h')      
  print(f'O valor da sua multa é de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança.\n')  
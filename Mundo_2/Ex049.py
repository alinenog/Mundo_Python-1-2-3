#Exercício Python 49:
# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

print('=-'*10)
print('      TABUADA')
print('=-'*10)
num = int(input('Digite o número que deseja ver a tabuada: '))     
for c in range(1, 11):
  print(f'{num} x {c} = {num*c}')        


#modelo de formatação 
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'. format(a,b))

#modelo de formatação 
nome = 'Aline'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;35m', nome,'\033[m'))

#modelo de formatação 
nome = 'Aline Nogueira'
print('Olá! Muito prazer em te conhecer, {}{}!!!'.format('\033[4;35m', nome,'\033[m'))

#modelo de formatação
nome = 'Aline Nogueira'
cores= {
  'limpa' : '\033[m',
  'azul' : '\033[34m',
  'vermelho':'\033[31m',
  'amarelo': '\033[33m',
  'pretoebranco': '\033[7;35m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['vermelho'], nome, cores['limpa']))
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
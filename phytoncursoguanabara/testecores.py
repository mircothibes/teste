a = 3
b = 4
print(f'A cor para teste \33[32m{a}\33[m e a cor para teste \33[31m{b}\33[m!!!')


nome = 'MIRCO'
cores = {'limpa':'\33[m',
         'azul':'\33[34m',
         'amarelo':'\33[33m',
         'pretoebranco':'\33[7;30m'}
print('Olá, muito prazer meu nome é,{}{}{}!!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
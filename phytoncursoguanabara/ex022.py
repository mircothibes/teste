'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome = str(input('Qual é o nome: ')).strip()
m = nome.upper()
mi = nome.lower()
ql = len(nome)-nome.count(' ')
fn = nome.find(' ')
print(f'Seu nome é {nome}\n'
      f'Seu nome em letras Maiusculas {m}\n'
      f'Seu nome em letras Minusculas {mi}\n'
      f'Seu nome tem {ql} letras\n'
      f'Seu primeiro nome tem {fn} letras')

''' Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

a = int(input('Numero um: '))
b = int(input('NUmero dois: '))
c = int(input('Numero três: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print(f'O menor valor digitado foi {menor}')

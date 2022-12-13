'''Crie um programa que leia quanto dinheiro uma pessoa
tem na carteira e mostre quantos dólares ela pode comprar.
considerando US$1,00 = R$5,40
'''

carteira = float(input('Quanto de dinhriro tem em sua carteira? R$'))
print('Voce tem US${:.2f}' .format(carteira / 5.40))




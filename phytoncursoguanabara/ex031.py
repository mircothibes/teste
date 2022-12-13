'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e
R$0,45 parta viagens mais longas.'''

distancia = float(input('Digite a distancia em Km'))
dc = distancia * 0.50
dl = distancia * 0.45
if distancia <= 200:
    print(f'O valor da passagem será de R${dc}')
else:
    print(f'O valor da passagem será de R${dl}')

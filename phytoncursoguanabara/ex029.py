'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = float(input('Qual a velocidade: '))
ultrapassou = (velocidade - 80) * 7
if velocidade > 80:
    print('Voce foi multado')
    print(f'Sua multa será de R${ultrapassou:.2f}.')
else:
    print('Sua velocidade esta no padrão')





'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('Sua nota foi {:.1f} que pe maior/igual que 7.0, sendo assim você está APROVADO!'.format(media))
elif media >= 5:
    print('Sua nota foi {:.1f} que é menor que 7.0, sendo assim você está em RECUPERAÇÃO!'.format(media))
elif media < 5:
    print('Sua nota foi {:.1f} que é menor que 5.0, sendo assim você está REPROVADO!'.format(media))

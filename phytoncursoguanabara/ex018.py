'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.'''

import math

angulo = float(input('Digite o angulo:º'))
seno = math.sin(math.radians(angulo))
print('O SENO de {:.0f} é {:.2f}'.format(angulo, seno))
cos = math.cos(math.radians(angulo))
print('O COSSENO de {:.0f} é {:.2f}'.format(angulo, cos))
tang = math.tan(math.radians(angulo))
print('A TANGENTE de {:.0f} é {:.2f}'.format(angulo, tang))





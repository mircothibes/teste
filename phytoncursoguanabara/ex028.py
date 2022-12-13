''' Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu'''

from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador pensar em um numero
print('=#=' * 25)
print('Vou pensar em numero entre 0 e 5, tente adivinhar qual...')
print('=#=' * 25)

jogador = int(input('Em que numero eu pensei? ')) #Jogador tenta adivinhar qual o numero
print('Processando.......')
sleep(3)
if jogador == computador:
    print('Parabéns! Você conseguiu vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e não no munero {}.'.format(computador, jogador))

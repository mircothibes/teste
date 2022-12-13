'''O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
import random
n1 = input('Digite um nome: ')
n2 = input('Digite um segundo nome: ')
n3 = input('Digite um terceiro nome: ')
n4 = input('Digite um quarto nome: ')

list = [n1, n2, n3, n4]
random.shuffle(list)
print('A ordem será')
print(list)





'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random
n1 = str(input('Nome primeiro aluno: '))
n2 = str(input('Nome segundo aluno: '))
n3 = str(input('Nome terçeiro aluno: '))
n4 = str(input('Nome quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O Aluno escolhido foi {}'.format(escolhido))








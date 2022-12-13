'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%'''

salario = float(input('Seu salario R$ '))
aumento = salario * 10 / 100 + salario
aumento2 = salario * 15 / 100 + salario
if salario > 1250:
    print('Seu salario atual é de R${:.2f} e com um aumento de 10% seu salario passara a se de R${:.2f}'. format(salario, aumento))
if salario <= 1250:
    print('Seu salario atual é de R${:.2f} e com um aumento de 15% seu salario será de R${:.2f}'. format(salario, aumento2))


salario = float(input('Seu salario R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, novo))


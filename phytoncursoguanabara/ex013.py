'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

salario_atual = float(input("Qual é seu salario atual: R$"))
aumento = salario_atual + (salario_atual*15/100)
print("Seu salario atual era de R${:.2f} e seu novo salario com aumento passará a se de R${:.2f}." .format(salario_atual, aumento))
